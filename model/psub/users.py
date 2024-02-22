from model.mechanism import creators
from model.types import FriendTechParams, FriendTechState, Signal, VariableUpdate
from model.storage import ext_storage
def p_user_update(params: FriendTechParams,
                     _2,
                     _3,
                     state: FriendTechState) -> Signal:
    timestep =state['timestep'] 
    if(timestep <= 1):
        ext_storage.init_active_user(params['user_scenario'],state['subset'])

    num_users = ext_storage.get_active_user_signal(state['subset'], timestep)
    return {'num_users': num_users}

def s_user_update(_1,
                    _2,
                    _3,
                    _4,
                    signal: Signal) -> VariableUpdate:
    return ('num_users', signal['num_users'])