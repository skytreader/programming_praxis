#! /usr/bin/env python3

import copy
import random
import unittest

"""
http://programmingpraxis.com/2009/12/11/selection/
UNFINISHED
"""

def partition(dataset, start_index=None, limit=None):
    """
    Partitions dataset. The dataset is modified in the function.
    Returns the post-partitioning index of the pivot used.Test
    with equal start_index and limit.
    """
    if start_index is None:
        start_index = 0

    if limit is None:
        limit = len(dataset)

    subdata = dataset[start_index:limit]
    pivot = random.choice(subdata)
    last_index = limit - 1
    pivot_index = -1
    
    i = start_index
    while i < limit:
        if pivot == dataset[i]:
            pivot_index = i
            break

        i += 1

    dataset[last_index], dataset[pivot_index] = dataset[pivot_index], dataset[last_index]
    pivot_index = last_index
    
    less_index = start_index - 1
    hi_index = less_index + 1

    while hi_index < last_index:
        if dataset[hi_index] < dataset[pivot_index]:
            less_index += 1
            dataset[less_index], dataset[hi_index] = dataset[hi_index], dataset[less_index]

        hi_index += 1

    less_index += 1
    dataset[less_index], dataset[pivot_index] = dataset[pivot_index], dataset[less_index]

    return less_index

def select(dataset, k):
    """
    Selects the kth percentile in the dataset.

    Assert:
        k <= len(dataset)
    """
    limit = len(dataset)
    if k > limit:
        raise IndexError("k should always be leq len(dataset)")
    
    partition_start = 0
    partition_limit = len(dataset)
    start = 0
    print("Virgin: " + str(dataset))
    while (limit - 1 - start) > 1:
        # What if we partition on the kth smallest item itself? :\
        partition_index = partition(dataset, start, limit)
        print(dataset)
        print(partition_index)
        smaller_len = partition_index - start + 1
        larger_len = limit - partition_index
        
        # What if one of the lens is equal to k?
        if smaller_len > k:
            limit = partition_index
        else:
            start = partition_index

    return dataset[start]

class FunctionsTest(unittest.TestCase):
    
    def partition_test(self):
        main_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        limit = len(main_list)

        l1 = copy.deepcopy(main_list)
        part_index1 = partition(l1)

        for i in range(part_index1):
            self.assertTrue(l1[part_index1] >= l1[i])

        i = part_index1 + 1
        while i < limit:
            self.assertTrue(l1[part_index1] <= l1[i])
            i += 1

        l2 = copy.deepcopy(main_list)
        part_index2 = partition(l2, 4, 9)

        i = 4

        while i < part_index2:
            self.assertTrue(l2[part_index2] >= l2[i])
            i += 1

        i = part_index2 + 1

        while i < limit:
            self.assertTrue(l2[part_index2] <= l2[i])
            i += 1
            

    def test_partition(self):
        for i in range(10):
            self.partition_test()

    def test_select(self):
        main_list = [3, 1, 4, 1, 5, 9, 2, 6, 5]
        # sorted this is [1, 1, 2, 3, 4, 5, 5, 6, 9]
        self.assertEqual(select(main_list, 5), 4)

if __name__ == "__main__":
    unittest.main()
