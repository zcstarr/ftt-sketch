import numpy as np
import math

def tokens_possible_for_purchase(y, supply):
    num_tokens = ((48000 * y) + math.pow(supply, 3)) ** (1/3)
    return num_tokens

def buy_curve(num_tokens,supply):
    y = math.pow(num_tokens + supply,3)/48000  - math.pow(supply,3)/48000
    return y

def sell_curve(num_tokens,supply):
    sell_tokens = min(num_tokens, supply)
    y = math.pow(supply,3)/48000 - math.pow(supply-sell_tokens,3)/48000
    return y

def get_fee(raw_price:float):
    return 0.10 * raw_price
