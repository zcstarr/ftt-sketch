from model.types import FriendTechParams, FriendTechState, Signal, VariableUpdate


def p_increment_time(params: FriendTechParams,
                     _2,
                     _3,
                     _4) -> Signal:
    timestep_in_days = params['timestep_in_days'] 
    return {'delta_in_days': timestep_in_days}


def s_days_passed(_1,
                  _2,
                  _3,
                  state: FriendTechState,
                  signal: Signal) -> VariableUpdate:
    value = state['days_passed']  + signal['delta_in_days']
    return ('days_passed', value)


def s_delta_days(_1,
                 _2,
                 _3,
                 _state: FriendTechState,
                 signal: Signal) -> VariableUpdate:
    value = signal['delta_in_days']
    return ('delta_days', value)