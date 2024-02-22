from dataclasses import dataclass
from typing import Any, Dict, List, Tuple, TypedDict

VariableUpdate = Tuple[str, object]
Signal = Dict[str, object]


@dataclass
class UserScenario:
    mu: float
    sigma: float
    initial_users: int
    num_timesteps: int

@dataclass
class PriceScenario:
    mu: float
    sigma: float
    initial_value: int
    num_timesteps: int



@dataclass
class Creator(TypedDict):
    id: int
    # probability of user churn
    churn_prob: float
    # percentage of user churn or users lost
    churn_percent: float
    # supply of keys in the system
    supply: float
    # amount of profit that capture
    profit: float
    # amount of stake that's captured
    stake: float
    reward: float

CreatorMap = Dict[int, Creator]
UserSignal = List[int]
UserSignals = Dict[int, UserSignal] 

class FriendTechState(TypedDict):
    days_passed: int
    delta_days: int
    ftt_price: float
    reward_tokens_issued: float
    num_users: int
    revenue: float
    creator_revenue: float
    creators: List[Creator]

class FriendTechParams(TypedDict):
    subset: int
    timestep: int
    timestep_in_days: int
    avg_churn_prob: float
    avg_churn_percent: float
    reward_margin: float
    creator_stake: float
    spend_limit: float
    num_creators: int
    user_scenario: UserScenario
    price_scenario: PriceScenario

class FriendTechParamsSweep(TypedDict):
    timestep_in_days: List[int]
    avg_churn_prob: List[float]
    avg_churn_percent: List[float]
    spend_limit: List[float]
    reward_margin: List[float]
    creator_stake: List[float]
    num_creators: List[int]
    user_scenario: List[UserScenario]
    price_scenario: List[PriceScenario]



@dataclass
class ExperimentArgs:
    initial_state:  FriendTechState 
    params: FriendTechParams 
    psubs: Any
    timesteps: int
    runs: int
