#! /usr/bin/env python3

import random
import sys
import unittest

"""
http://programmingpraxis.com/2011/09/23/array-duplicates/
UNFINISHED
"""

def detect_duplicate(numberset):
    return 0

class FunctionsTest(unittest.TestCase):
    
    def __create_test_array(self):
        """
        Choose 999,999 unique random numbers from 0 to 3 million. Then, pick
        a random value from the unique 999,999. Returns an array with two
        values: the first one is the test array, the second one is the 
        """
        test_array = []

        for i in range(999,999):
            rand_num = random.randint(0, 3000001)

            while rand_num in test_array:
                rand_num = random.randint(0, 3000001)

            test_array.append(rand_num)

        test_array.append(random.choice(test_array))

        return test_array

    def test_detect_duplicate(self):
        for i in range(100):
            test_array = self.__create_test_array()
