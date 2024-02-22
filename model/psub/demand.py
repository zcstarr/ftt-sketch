import math
from model.types import FriendTechParams, FriendTechState, Signal
from model.storage import ext_storage
from model.mechanism import curve,demand
import numpy as np

def p_key_buy(params: FriendTechParams,
                   _1,
                   _2,
                   state: FriendTechState) -> Signal:
    creators = state['creators']
    revenue = state['revenue']
    num_users = ext_storage.get_active_user_signal(state['subset'], state['timestep'])
    spend_per_user = demand.gen_spend(num_users, params['spend_limit'])
    chosen_creators = np.random.choice(creators, size=num_users, replace=True)
    for (i, spend) in enumerate(spend_per_user):
        creator = chosen_creators[i]
        id = creator['id']
        fee = curve.get_fee(spend)
        new_supply = curve.buy_curve(abs(spend), creators[id]['supply'])
        creators[id]['supply'] = new_supply + creators[id]['supply']
        creators[id]['profit'] = creators[id]['profit'] + fee/2
        revenue = revenue + fee/2  
    return {'revenue': revenue, 'creators': creators}

def p_key_churn(params: FriendTechParams,
                   _1,
                   _2,
                   state: FriendTechState) -> Signal:
    creators = state['creators']
    revenue = 0 
    for c in creators:
        # assummes fee is paid on top
        if c['churn_prob'] > np.random.random():
            num_tokens = math.ceil(c['churn_percent'] * c['supply'])
            sell_tokens = min(num_tokens, c['supply'])
            ftt_tokens = curve.sell_curve(sell_tokens, c['supply'])
            fee = curve.get_fee(ftt_tokens)
            creator_profit =  c['profit'] + fee/2 
            revenue = revenue + fee/2
            c['supply'] = max(c['supply'] - sell_tokens,0)
            c['profit'] = creator_profit
        
    return {'revenue': revenue, 'creators': creators}

def s_revenue( _1,
        _2,
        _3,
        state: FriendTechState,
        signal: Signal) -> Signal:
    return ('revenue', signal['revenue'])


def s_price_update(_1,
                   _2,
                   _3,
                   state: FriendTechState,
                   signal: Signal) -> Signal:

    return ('ftt_price', signal['ftt_price'])