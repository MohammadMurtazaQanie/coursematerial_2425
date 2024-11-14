import math

def internet_costs(duration_in_seconds, cost_per_block):
    num_blocks = math.ceil(duration_in_seconds / 360)
    return num_blocks * cost_per_block