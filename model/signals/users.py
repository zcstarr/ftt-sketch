from dataclasses import dataclass
from typing import List
import numpy as np


def gen_daily_active_user_signal(mu: float, sigma: float, initial_users: int, num_timesteps: int) -> List[int]:
    # Start with the initial number of users in log space to prevent overflow
    log_daily_active_users = [np.log(initial_users)]
    
    for _ in range(1, num_timesteps):
        # Generate a change using a Gaussian distribution
        change = np.random.normal(mu, sigma)
        
        # Update the log of users directly to simulate growth or decline
        log_new_users = log_daily_active_users[-1] + change
        
        # Ensure the result is positive by converting log space to linear space and rounding
        new_users = int(np.round(np.exp(log_new_users)))
        
        # Append the updated number of users (in linear space) to the list
        log_daily_active_users.append(log_new_users)
    
    # Convert all log values back to linear space for the final output
    daily_active_users = [int(np.round(np.exp(log_user))) for log_user in log_daily_active_users]
    
    return daily_active_users    