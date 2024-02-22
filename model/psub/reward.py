
from model.types import FriendTechParams, FriendTechState, Signal


def p_reward_tokens(params: FriendTechParams,
                   _1,
                   _2,
                   state: FriendTechState) -> Signal:
    total_rewards_tokens = 0
    creators = state['creators']
    total_supply = sum([c['supply'] for c in creators])
    total_stake = sum([c['stake'] for c in creators])
    for i, c in enumerate(creators):
        supply_weight = c['supply']/total_supply
        stake_weight =  c['stake']/total_stake
        cost_in_tokens = params['daily_cost']/state['ftt_price']

        reward_tokens = (supply_weight * cost_in_tokens) + (max(stake_weight,0.20)* cost_in_tokens)
        reward_tokens = reward_tokens + (params['reward_margin'] * cost_in_tokens)

        total_rewards_tokens = total_rewards_tokens + reward_tokens
        c['reward'] = reward_tokens + c['reward']

    return {'creators': creators, 'total_rewards_tokens': total_rewards_tokens}

def s_reward_tokens(_1,
                   _2,
                   _3,
                   state: FriendTechState,
                   signal: Signal) -> Signal:
    return ('reward_tokens_issued', signal['total_rewards_tokens'])