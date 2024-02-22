from typing import List, TypedDict

import pandas as pd
from model.types import Creator, CreatorMap
from model import types
from model.signals import users, generic

CREATOR_MAP = {}
crx = Creator()
INDIVIDUAL_CREATOR_DATA = []
def fill_creator_map(creators: List[Creator]) -> CreatorMap:
    for creator in creators:
        CREATOR_MAP[creator['id']] = creator
    return CREATOR_MAP

def get_creator_map():
    return CREATOR_MAP

def track_creator(creators: List[Creator], timestep) -> pd.DataFrame:
    global INDIVIDUAL_CREATOR_DATA
    if(len(creators)) <= 0:
        return INDIVIDUAL_CREATOR_DATA
    else:
        for creator in creators:
            creator['timestep'] = timestep
            INDIVIDUAL_CREATOR_DATA.append(creator)
        return INDIVIDUAL_CREATOR_DATA

def get_creator_data():
    global INDIVIDUAL_CREATOR_DATA
    return pd.DataFrame(INDIVIDUAL_CREATOR_DATA,columns=['timestep'].extend(crx.keys()))

USER_SIGNALS = {}

def init_active_user(user_scenario: types.UserScenario, control: int):
    global USER_SIGNALS
    USER_SIGNALS[control] = users.gen_daily_active_user_signal(
        user_scenario.mu,
        user_scenario.sigma,
        user_scenario.initial_users,
        user_scenario.num_timesteps
    )

def get_active_user_signal(control: int, timestep: int):
    global USER_SIGNALS
    # time starts at 1, 0 is used for initialization
    if(timestep < 1): 
        return []

    return USER_SIGNALS[control][timestep-1]
    
PRICE_SIGNALS = {}
def init_price_signal(price_scenario: types.PriceScenario, control: int):
    global PRICE_SIGNALS 
    PRICE_SIGNALS[control] = generic.gen_daily_value(
        price_scenario.mu,
        price_scenario.sigma,
        price_scenario.initial_value,
        price_scenario.num_timesteps
    )

def get_price_signal(control: int, timestep: int):
    global PRICE_SIGNALS
    # time starts at 1, 0 is used for initialization
    if(timestep < 1): 
        return []
    return PRICE_SIGNALS[control][timestep-1]
 
