#! /usr/bin/env python3

import math

"""
http://programmingpraxis.com/2010/09/21/kaprekar-numbers/
"""

def is_kaprekar(num):
    """
    Expects an integer.
    """
    square = num ** 2
    numstring = str(square)
    digit_count = len(numstring)
    divide_index = math.floor(digit_count / 2)
    first_half = numstring[0:divide_index]
    second_half = numstring[divide_index:digit_count]
    
    try:
        return (int(first_half) + int(second_half)) == num
    except ValueError:
        return False

if __name__ == "__main__":
    for i in range(1000):
        if is_kaprekar(i):
            print(i)
