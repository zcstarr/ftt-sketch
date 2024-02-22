from model.mechanism import creators
from model.types import FriendTechParams, FriendTechState, Signal, VariableUpdate
from model.storage import ext_storage
def p_gen_population(params: FriendTechParams,
                     _2,
                     _3,
                     state: FriendTechState) -> Signal:
    timestep =state['timestep'] 
    if(timestep == 0):
        clist = creators.gen_population(params['num_creators'], params['avg_churn_prob'], params['avg_churn_percent'], params['creator_stake'])
        ext_storage.fill_creator_map(clist)
    else: 
        clist = state['creators']
    ext_storage.track_creator(clist, timestep)
    return {'creators': clist}

def s_gen_population(_1,
                    _2,
                    _3,
                    _4,
                    signal: Signal) -> VariableUpdate:
    return ('creators', signal['creators'])

def s_update_creators(_1,
                    _2,
                    _3,
                    state: FriendTechState,
                    signal: Signal) -> VariableUpdate:
    return ('creators', signal['creators'])

def s_update_creators_metric(_1,
                    _2,
                    _3,
                    state: FriendTechState,
                    signal: Signal) -> VariableUpdate:
    ext_storage.track_creator(signal['creators'], state['timestep'])
    return ('creators', signal['creators'])
