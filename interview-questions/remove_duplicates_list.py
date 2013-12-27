#! /usr/bin/env python3

import random
import unittest

"""
http://programmingpraxis.com/2013/12/17/remove-duplicates-from-a-list/

The problem statement is:
    Return a list containing only one copy of any duplicates in an input list,
    with items in the output in the same order as their first appearance in the
    input.

There are two interpretations to this problem: (1) copy the list removing all
duplicates or, the one I took, (2) get the set of all duplicating items in the
list and return them in the order their first instance appeared in the list.
"""

def aux_list(l):
    aux_list = []
    duplicates_list = []

    for item in l:
        if item in aux_list and item not in duplicates_list:
            duplicates_list.append(item)
        else:
            aux_list.insert(0, item)

    return duplicates_list

def aux_map(l):
    count_map = {}
    duplicates_list = []

    for item in l:
        if count_map.get(item):
            count_map[item] += 1
        else:
            count_map[item] = 1
        
        if count_map[item] >= 2 and item not in duplicates_list:
            duplicates_list.append(item)

    return duplicates_list

class FunctionsTest(unittest.TestCase):
    
    def test_deterministic(self):
        # Elements repeat at most once
        atmostonce = [1, 5, 5, 3, 8, 2, 11, 2, 7, 10, 14, 7]
        atmostonce_ans = [5, 2, 7]
        
        self.assertEqual(aux_list(atmostonce), atmostonce_ans)
        self.assertEqual(aux_map(atmostonce), atmostonce_ans)

        # Elements repeat more than once
        pi_test = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7]
        pi_answer = [1, 5, 3, 9]

        self.assertEqual(aux_list(pi_test), pi_answer)
        self.assertEqual(aux_map(pi_test), pi_answer)

        # No repeating elements at all
        norepeat = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        norepeat_ans = []

        self.assertEqual(aux_list(norepeat), norepeat_ans)
        self.assertEqual(aux_map(norepeat), norepeat_ans)

    def test_random(self):
        pool = range(500)
        iterations = range(1000)
        for i in iterations:
            # Construct random list
            test = [random.choice(pool) for j in iterations]
            self.assertEqual(aux_list(test), aux_map(test))

if __name__ == "__main__":
    unittest.main()
