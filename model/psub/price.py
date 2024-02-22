from model.types import FriendTechParams, FriendTechState, Signal
from model.storage import ext_storage


def p_price_update(params: FriendTechParams,
                   _1,
                   _2,
                   state: FriendTechState) -> Signal:
    if(state['timestep'] <= 1):
        ext_storage.init_price_signal(params['price_scenario'], state['subset'])
    price = ext_storage.get_price_signal(state['subset'], state['timestep'])
    return {'ftt_price': price}

def s_price_update(_1,
                   _2,
                   _3,
                   state: FriendTechState,
                   signal: Signal) -> Signal:

    return ('ftt_price', signal['ftt_price'])