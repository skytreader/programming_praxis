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
    """
    Remove everything in l2 from l1.
    """
    diffed = [item for item in l1]

    for item in l2:
        if item in l1:
            diffed.remove(item)

    return diffed

class FunctionsTest(unittest.TestCase):
    
    def setUp(self): 
        # Standard tests
        self.la = [4, 7, 12, 6, 17, 5, 13]
        self.lb = [7, 19, 4, 11, 13, 2, 15]
        self.intersection = set([4, 7, 13])
        self.union = set([4, 7, 12, 6, 17, 5, 13, 19, 11, 2, 15])
        self.ab_difference = set([12, 6, 17, 5])
        self.ba_difference = set([19, 11, 2, 15])

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
    
    def test_difference(self):
        self.assertEqual(set(difference(self.la, self.lb)), self.ab_difference)
        self.assertEqual(set(difference(self.lb, self.la)), self.ba_difference)
        self.assertEqual(set(difference(self.small_list, self.large_list)), set())
        self.assertEqual(set(difference(self.large_list, self.small_list)), set([4, 5]))

if __name__ == "__main__":
    unittest.main()
