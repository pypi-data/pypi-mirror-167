import os
import sys
import traceback
import tempfile
from pathlib import Path
import json
import requests
from datetime import datetime

import pandas as pd
from pandas.core.frame import DataFrame
import torch.multiprocessing as mp
import lightwood
from lightwood.api.types import ProblemDefinition, JsonAI
from lightwood import __version__ as lightwood_version

from mindsdb import __version__ as mindsdb_version
import mindsdb.interfaces.storage.db as db
from mindsdb.interfaces.storage.db import session, Predictor
from mindsdb.interfaces.storage.fs import FsStore
from mindsdb.utilities.config import Config
from mindsdb.utilities.functions import mark_process
from mindsdb.utilities.log import log
from mindsdb.integrations.libs.const import PREDICTOR_STATUS


ctx = mp.get_context('spawn')


def create_learn_mark():
    if os.name == 'posix':
        p = Path(tempfile.gettempdir()).joinpath('mindsdb/learn_processes/')
        p.mkdir(parents=True, exist_ok=True)
        p.joinpath(f'{os.getpid()}').touch()


def delete_learn_mark():
    if os.name == 'posix':
        p = Path(tempfile.gettempdir()).joinpath('mindsdb/learn_processes/').joinpath(f'{os.getpid()}')
        if p.exists():
            p.unlink()


def rep_recur(org: dict, ovr: dict):
    for k in ovr:
        if k in org:
            if isinstance(org[k], dict) and isinstance(ovr[k], dict):
                rep_recur(org[k], ovr[k])
            else:
                org[k] = ovr[k]
        else:
            org[k] = ovr[k]


def brack_to_mod(ovr):
    if not isinstance(ovr, dict):
        if isinstance(ovr, list):
            for i in range(len(ovr)):
                ovr[i] = brack_to_mod(ovr[i])
        elif isinstance(ovr, str):
            if '(' in ovr and ')' in ovr:
                mod = ovr.split('(')[0]
                args = {}
                if '()' not in ovr:
                    for str_pair in ovr.split('(')[1].split(')')[0].split(','):
                        k = str_pair.split('=')[0].strip(' ')
                        v = str_pair.split('=')[1].strip(' ')
                        args[k] = v

                ovr = {
                    'module': mod,
                    'args': args
                }
            elif '{' in ovr and '}' in ovr:
                try:
                    ovr = json.loads(ovr)
                except Exception:
                    pass
        return ovr
    else:
        for k in ovr.keys():
            ovr[k] = brack_to_mod(ovr[k])

    return ovr


@mark_process(name='learn')
def run_generate(df: DataFrame, problem_definition: ProblemDefinition, predictor_id: int, json_ai_override: dict = None):
    json_ai = lightwood.json_ai_from_problem(df, problem_definition)
    if json_ai_override is None:
        json_ai_override = {}

    json_ai_override = brack_to_mod(json_ai_override)
    json_ai = json_ai.to_dict()
    rep_recur(json_ai, json_ai_override)
    json_ai = JsonAI.from_dict(json_ai)

    code = lightwood.code_from_json_ai(json_ai)

    predictor_record = Predictor.query.with_for_update().get(predictor_id)
    predictor_record.json_ai = json_ai.to_dict()
    predictor_record.code = code
    db.session.commit()


@mark_process(name='learn')
def run_fit(predictor_id: int, df: pd.DataFrame) -> None:
    try:
        predictor_record = Predictor.query.with_for_update().get(predictor_id)
        assert predictor_record is not None

        fs_store = FsStore()
        config = Config()

        predictor_record.data = {'training_log': 'training'}
        predictor_record.status = PREDICTOR_STATUS.TRAINING
        db.session.commit()
        predictor: lightwood.PredictorInterface = lightwood.predictor_from_code(predictor_record.code)
        predictor.learn(df)

        db.session.refresh(predictor_record)

        fs_name = f'predictor_{predictor_record.company_id}_{predictor_record.id}'
        pickle_path = os.path.join(config['paths']['predictors'], fs_name)
        predictor.save(pickle_path)

        fs_store.put(fs_name, base_dir=config['paths']['predictors'])

        predictor_record.data = predictor.model_analysis.to_dict()

        # getting training time for each tried model. it is possible to do
        # after training only
        fit_mixers = list(predictor.runtime_log[x] for x in predictor.runtime_log
                          if isinstance(x, tuple) and x[0] == "fit_mixer")
        submodel_data = predictor_record.data.get("submodel_data", [])
        # add training time to other mixers info
        if submodel_data and fit_mixers and len(submodel_data) == len(fit_mixers):
            for i, tr_time in enumerate(fit_mixers):
                submodel_data[i]["training_time"] = tr_time
        predictor_record.data["submodel_data"] = submodel_data

        predictor_record.dtype_dict = predictor.dtype_dict
        db.session.commit()
    except Exception as e:
        db.session.refresh(predictor_record)
        predictor_record.data = {'error': f'{traceback.format_exc()}\nMain error: {e}'}
        db.session.commit()
        raise e


@mark_process(name='learn')
def run_learn_remote(df: DataFrame, predictor_id: int) -> None:
    try:
        serialized_df = json.dumps(df.to_dict())
        predictor_record = Predictor.query.with_for_update().get(predictor_id)
        resp = requests.post(predictor_record.data['train_url'],
                             json={'df': serialized_df, 'target': predictor_record.to_predict[0]})

        assert resp.status_code == 200
        predictor_record.data['status'] = 'complete'
    except Exception:
        predictor_record.data['status'] = 'error'
        predictor_record.data['error'] = str(resp.text)

    session.commit()


def format_exception_error(exception):
    try:
        exception_type, _exception_object, exception_traceback = sys.exc_info()
        filename = exception_traceback.tb_frame.f_code.co_filename
        line_number = exception_traceback.tb_lineno
        error_message = f'{exception_type.__name__}: {exception}, raised at: {filename}#{line_number}'
    except Exception:
        error_message = str(exception)
    return error_message


@mark_process(name='learn')
def run_learn(df: DataFrame, problem_definition: ProblemDefinition, predictor_id: int,
              json_ai_override: dict = None) -> None:
    if json_ai_override is None:
        json_ai_override = {}

    predictor_record = Predictor.query.with_for_update().get(predictor_id)
    predictor_record.training_start_at = datetime.now()
    db.session.commit()

    try:
        run_generate(df, problem_definition, predictor_id, json_ai_override)
        run_fit(predictor_id, df)
    except Exception as e:
        predictor_record = Predictor.query.with_for_update().get(predictor_id)
        print(traceback.format_exc())

        error_message = format_exception_error(e)

        predictor_record.data = {"error": error_message}
        predictor_record.status = PREDICTOR_STATUS.ERROR
        db.session.commit()

    predictor_record.training_stop_at = datetime.now()
    predictor_record.status = PREDICTOR_STATUS.COMPLETE
    db.session.commit()


def run_adjust(name, db_name, from_data, datasource_id, company_id):
    # @TODO: Actually implement this
    return 0


@mark_process(name='learn')
def run_update(predictor_id: str, df: DataFrame, company_id: int):
    fs_store = FsStore()
    config = Config()

    try:
        old_predictor_record = Predictor.query.filter_by(id=predictor_id).first()
        assert old_predictor_record is not None
        old_predictor_record.update_status = 'updating'
        session.commit()

        predictor_record = db.Predictor(
            company_id=company_id,
            name=old_predictor_record.name,
            integration_id=old_predictor_record.integration_id,
            data_integration_id=old_predictor_record.data_integration_id,
            fetch_data_query=old_predictor_record.fetch_data_query,
            mindsdb_version=mindsdb_version,
            lightwood_version=lightwood_version,
            to_predict=old_predictor_record.to_predict,
            learn_args=old_predictor_record.learn_args,
            data={'name': old_predictor_record.name},
            training_data_columns_count=len(df.columns),
            training_data_rows_count=len(df),
            training_start_at=datetime.now(),
            active=False,
            status=PREDICTOR_STATUS.GENERATING
        )
        session.add(predictor_record)
        session.commit()

        problem_definition = predictor_record.learn_args
        problem_definition['target'] = predictor_record.to_predict[0]

        if 'join_learn_process' in problem_definition:
            del problem_definition['join_learn_process']

        if 'stop_training_in_x_seconds' in problem_definition:
            problem_definition['time_aim'] = problem_definition['stop_training_in_x_seconds']

        json_ai = lightwood.json_ai_from_problem(df, problem_definition)
        predictor_record.json_ai = json_ai.to_dict()
        predictor_record.code = lightwood.code_from_json_ai(json_ai)
        predictor_record.data = {'training_log': 'training'}
        session.commit()
        predictor: lightwood.PredictorInterface = lightwood.predictor_from_code(predictor_record.code)
        predictor.learn(df)

        fs_name = f'predictor_{predictor_record.company_id}_{predictor_record.id}'
        pickle_path = os.path.join(config['paths']['predictors'], fs_name)
        predictor.save(pickle_path)
        fs_store.put(fs_name, base_dir=config['paths']['predictors'])
        predictor_record.data = predictor.model_analysis.to_dict()
        predictor_record.update_status = 'up_to_date'
        predictor_record.dtype_dict = predictor.dtype_dict
        old_predictor_record.update_status = 'up_to_date'

        old_predictor_record.active = False
        predictor_record.active = True
        session.commit()
    except Exception as e:
        log.error(e)
        predictor_record = Predictor.query.with_for_update().get(predictor_id)
        print(traceback.format_exc())

        error_message = format_exception_error(e)

        predictor_record.data = {"error": error_message}

        old_predictor_record.update_status = 'update_failed'   # TODO
        db.session.commit()

    predictor_record.training_stop_at = datetime.now()
    db.session.commit()


class LearnRemoteProcess(ctx.Process):
    deamon = True

    def __init__(self, *args):
        super(LearnRemoteProcess, self).__init__(args=args)

    def run(self):
        run_learn_remote(*self._args)


class LearnProcess(ctx.Process):
    daemon = True

    def __init__(self, *args):
        super(LearnProcess, self).__init__(args=args)

    def run(self):
        run_learn(*self._args)


class GenerateProcess(ctx.Process):
    daemon = True

    def __init__(self, *args):
        super(GenerateProcess, self).__init__(args=args)

    def run(self):
        run_generate(*self._args)


class FitProcess(ctx.Process):
    daemon = True

    def __init__(self, *args):
        super(FitProcess, self).__init__(args=args)

    def run(self):
        run_fit(*self._args)


class AdjustProcess(ctx.Process):
    daemon = True

    def __init__(self, *args):
        super(AdjustProcess, self).__init__(args=args)

    def run(self):
        '''
        running at subprocess due to
        ValueError: signal only works in main thread

        this is work for celery worker here?
        '''
        run_adjust(*self._args)


class UpdateProcess(ctx.Process):
    daemon = True

    def __init__(self, *args):
        super(UpdateProcess, self).__init__(args=args)

    def run(self):
        run_update(*self._args)
