import math
import numpy as np
from cadCAD_tools.preparation import sweep_cartesian_product

from model import types

DAYS_PER_TIMESTEP = 1
YEAR = 365.25
SIMULATION_TIME_IN_YEARS = 1
DEFAULT_RUNS = 1
DEFAULT_TIMESTEPS = int(math.ceil(SIMULATION_TIME_IN_YEARS * YEAR) / DAYS_PER_TIMESTEP)



RAW_PARAMS = types.FriendTechParamsSweep(
    timestep_in_days=[1],
    # 0.14 is a person a week
    avg_churn_prob=[0.14],
    # 10% of your key supply
    avg_churn_percent=[0.1],
    creator_stake=[1000],
    num_creators=[1000],
    # 90 a month average Patreon creator value
    daily_cost = [3],
    # limit in tokens
    spend_limit = [0.1],
    reward_margin=[1.30],
    # we're using eth adjacent pricing due to bonding curve
    # structure
    price_scenario=[types.PriceScenario(
        mu=0.001,
        sigma=0.01,
        initial_value=1000.0,
        num_timesteps=DEFAULT_TIMESTEPS
    )],
    user_scenario=[types.UserScenario(
        mu=0.001,
        sigma=0.001,
        initial_users=10000,
        num_timesteps=DEFAULT_TIMESTEPS
    )]
)

PARAMS = sweep_cartesian_product(RAW_PARAMS)

DEFAULT_INITIAL_STATE = types.FriendTechState(
    days_passed=0,
    delta_days=DAYS_PER_TIMESTEP,
    ftt_price = 0.0,
    num_users=0,
    creators = [],
    # assume tokens initially distributed are accounted for
    reward_tokens_issued = 0,
    revenue=0
)
