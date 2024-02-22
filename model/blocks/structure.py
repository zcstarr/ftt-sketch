from model.psub import time,creators,price,users,demand,reward
from model.types import PriceScenario

BLOCKS = [
    {
        'label': 'Time Tracking',
        'policies': {
            'increment_time': time.p_increment_time,
            'create_population': creators.p_gen_population,
        },
        'variables': {
            'days_passed': time.s_days_passed,
            'delta_days': time.s_delta_days,
            'creators': creators.s_gen_population,
        }
    },
    {
        'label': 'Price & demand tracking',
        'policies': {
            'ftt_price':price.p_price_update,
            'num_users': users.p_user_update,
        },
        'variables': {
            'ftt_price': price.s_price_update,
            'num_users': users.s_user_update,
        }
    },
    {
        'label': 'Churn',
        'policies': {
            'churn': demand.p_key_churn,
        },
        'variables': {
            'creators': creators.s_update_creators,
            'revenue': demand.s_revenue,
        }
    },
    {
        'label': 'Purchase',
        'policies': {
            'key_purchase': demand.p_key_buy
        },
        'variables': {
            'creators': creators.s_update_creators,
            'revenue': demand.s_revenue,
        }
    },
    {
        'label': 'Reward',
        'policies': {
            'reward_tokens': reward.p_reward_tokens,
        },
        'variables': {
            'reward_tokens_issued': reward.s_reward_tokens,
            'creators': creators.s_update_creators,
        }

    }
    

]
