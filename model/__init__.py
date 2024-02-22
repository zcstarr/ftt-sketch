from model.params import PARAMS, DEFAULT_INITIAL_STATE, DEFAULT_TIMESTEPS, DEFAULT_RUNS
from model.types import ExperimentArgs
from model.blocks.structure import BLOCKS

default_exp_args = ExperimentArgs(initial_state=DEFAULT_INITIAL_STATE,
                                  params=PARAMS,
                                  psubs=BLOCKS,
                                  timesteps=DEFAULT_TIMESTEPS,
                                  runs=DEFAULT_RUNS)

default_dev_args = ExperimentArgs(initial_state=DEFAULT_INITIAL_STATE,
                                  params=PARAMS,
                                  psubs=BLOCKS,
                                  timesteps=3,
                                  runs=1)