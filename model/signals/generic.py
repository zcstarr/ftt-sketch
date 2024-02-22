from dataclasses import dataclass
from typing import List
import numpy as np


def gen_daily_value(mu: float, sigma: float, initial_value: float, num_timesteps: int) -> List[float]:
    # Start with the initial value in log space to prevent overflow
    log_daily_values = [np.log(initial_value)]
    
    for _ in range(1, num_timesteps):
        # Generate a change using a Gaussian distribution
        change = np.random.normal(mu, sigma)
        
        # Update the log of values directly to simulate growth or decline
        log_new_value = log_daily_values[-1] + change
        
        # Ensure the result is positive by converting log space to linear space
        new_value = np.exp(log_new_value)
        
        # Append the updated value (in linear space) to the list
        log_daily_values.append(log_new_value)
    
    # Convert all log values back to linear space for the final output
    daily_values = [np.exp(log_value) for log_value in log_daily_values]
    
    return daily_values