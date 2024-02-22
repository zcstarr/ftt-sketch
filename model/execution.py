from typing import Callable, Union
import pandas as pd
from cadCAD_tools.execution import easy_run
import model.types as types
import model
import model.params as params
import os
from datetime import datetime
import dill
import gzip
# cribbed from Dan Lessa cadcad patch

def execute_experiment(experiment_args: types.ExperimentArgs = model.default_exp_args, profile: bool = False):
    return easy_run(experiment_args.initial_state,
                    experiment_args.params,
                    experiment_args.psubs,
                    experiment_args.timesteps,
                    experiment_args.runs,
                    exec_mode='local',
                    drop_substeps=True)


def save_execution(df, timestamp=datetime.now().strftime("%Y-%m-%d_%H-%M-%S"), prefix="single-run", ):
    data_dir = 'data/simulations'
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    with gzip.open(f"{data_dir}/single-run-{timestamp}.pkl.gz", 'wb') as f:
        dill.dump(df, f)