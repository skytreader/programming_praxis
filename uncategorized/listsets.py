#! /usr/bin/env python3

import unittest

"""
http://programmingpraxis.com/2012/11/16/list-intersection-and-union/
http://programmingpraxis.com/2012/11/20/list-difference/

Code without using sets.

UNFINISHED
"""

def intersection(l1, l2):
    smaller_len = min(len(l1), len(l2))
    smaller_list = l1 if len(l1) == smaller_len else l2
    larger_list = l2 if smaller_list == l1 else l1
    intersection = []

    for item in smaller_list:
        if item in larger_list:
            intersection.append(item)

    return intersection

def union(l1, l2):
    union = [item for item in l1]

    for item in l2:
        if item not in union:
            union.append(item)

    return union

def difference(l1, l2):
    larger_len = max(len(l1), len(l2))
    larger_list = l1 if len(l1) == larger_len else l2
    smaller_list = l2 if larger_list == l1 else l1
    difference = []

    for item in larger_list:
        if item not in smaller_list:
            difference.append(item)

    return difference

class FunctionsTest(unittest.TestCase):
    
    def setUp(self): 
        # Standard tests
        self.la = [4, 7, 12, 6, 17, 5, 13]
        self.lb = [7, 19, 4, 11, 13, 2, 15]
        self.intersection = set([4, 7, 13])
        self.union = set([4, 7, 12, 6, 17, 5, 13, 19, 11, 2, 15])

        self.small_list = [1, 2, 3]
        self.large_list = [1, 2, 3, 4, 5]
        self.sl_intersection = set([1, 2, 3])
        self.sl_union = set([1, 2, 3, 4, 5])

    def test_intersection(self):
        list_intersection = set(intersection(self.la, self.lb))
        self.assertEqual(list_intersection, self.intersection)

        sl_intersection = set(intersection(self.small_list, self.large_list))
        self.assertEqual(self.sl_intersection, sl_intersection)

    def test_union(self):
        self.assertEqual(set(union(self.la, self.lb)), self.union)
        self.assertEqual(set(union(self.small_list, self.large_list)), self.sl_union)

if __name__ == "__main__":
    unittest.main()
