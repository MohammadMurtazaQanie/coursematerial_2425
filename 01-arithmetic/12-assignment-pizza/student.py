import math


def pizza(n_people, slices_per_pizza):
    return math.ceil (n_people // slices_per_pizza)