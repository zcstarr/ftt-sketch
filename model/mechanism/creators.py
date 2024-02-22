import numpy as np
from typing import List
from model.types import Creator
from scipy.stats import truncnorm

# takes average churn probability, churn percent, and stake
def gen_population(num_creators: float, churn_prob: float, churn_percent:float, stake: float) -> List[Creator]:
    creators = []
    cr_churn_prob = np.random.normal(churn_prob,churn_prob/6,num_creators)
    cr_churn_per = np.random.normal(churn_prob,churn_percent/6,num_creators)
    cr_stake = np.random.normal(stake,churn_percent/6,num_creators)
    for i in range(int(num_creators)):
        creator = Creator(id=i, churn_prob=cr_churn_prob[i], churn_percent=cr_churn_per[i], supply=0, profit=0, reward=0, stake=cr_stake[i])
        creators.append(creator)
    return creators
