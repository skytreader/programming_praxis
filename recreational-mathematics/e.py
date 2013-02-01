#! /usr/bin/env python3

import random

"""
http://programmingpraxis.com/2010/08/13/e/
"""

def random_to_one():
    """
    Generates random numbers until they sum up
    to more than 1. Returns the number of random
    numbers generated.
    """
    running_sum = 0
    rand_count = 0

    while running_sum < 1:
        running_sum += random.random()
        rand_count += 1

    return rand_count

def get_ave(count):
    running_sum = 0
    
    for i in range(count):
        running_sum += random_to_one()

    return running_sum / count

if __name__ == "__main__":
    print(get_ave(1000))
