#! /usr/bin/env python3

import unittest

"""
http://programmingpraxis.com/2011/04/01/maximum-difference-in-an-array/
UNFINISHED

TODO: Test this on a monotonically decreasing list.
"""

def max_diff_quad(numlist):
    """
    Returns a tuple containing the ith and jth element
    that produces the maximum difference. Runs in quadratic
    time.

    Description:
    Naive solution that checks for all possible differences
    and takes note of the maximum.
    """
    limit = len(numlist)
    maxdiff = float("-inf")
    maxi = -1
    maxj = -1

    for i in range(limit):
        j = i + 1 

        while j < limit:
            if (numlist[j] - numlist[i]) > maxdiff:
                maxdiff = numlist[j] - numlist[i]
                maxi = i
                maxj = j

            j += 1
    
    return (maxi, maxj)

def max_diff_lin(numlist):
    """
    Returns a tuplle containing the ith and jth element
    that produces the maximum difference. Runs in linear
    time.

    Description:
    Notice that, for every number x_k in numlist, it's pair
    x_l that gives it its maximum difference is the largest
    number to it's right. Therefore, to get x_i and x_j, first
    find the minimum number in the list; this is x_i. x_j will
    be the largest number at the right of x_i . This gives two
    O(n) scans == O(n) .

    Problems:
     - Satisfy the "leftmost shortest" rule.
     - Monotonically decreasing seq.
    """
    # OK...not very optimal but just to get my point.
    limit = len(numlist)

    maxmember = max(numlist)
    maxdex = numlist.index(maxmember)
    minpair = min(numlist[0:maxdex + 1])
    minpair_index = numlist.index(minpair)

    minmember = min(numlist)
    mindex = numlist.index(minmember)
    maxpair = max(numlist[mindex:limit-1])
    maxpair_index = numlist.index(maxpair)

    diff1 = numlist[maxdex] - numlist[minpair_index]
    diff2 = numlist[maxpair_index] - numlist[mindex]

    if diff1 > diff2:
        return (minpair_index, maxdex)
    elif diff1 < diff2:
        return (mindex, maxpair_index)
    else:
        return (minpair_index, maxdex) if minpair_index < mindex else (mindex, maxpair_index)

class FunctionsTest(unittest.TestCase):
    
    def test_quad(self):
        self.assertEqual((3, 4), max_diff_quad([4,3,9,1,8,2,6,7,5]))
        self.assertEqual((1, 2), max_diff_quad([4,2,9,1,8,3,6,7,5]))

    def test_lin(self):
        self.assertEqual((3, 4), max_diff_lin([4,3,9,1,8,2,6,7,5]))
        self.assertEqual((1, 2), max_diff_lin([4,2,9,1,8,3,6,7,5]))
        self.assertEqual((3, 7), max_diff_lin([4,3,9,1,2,6,7,8,5]))
        self.assertEqual((0, 0), max_diff_lin([5,4,3,2,1]))

if __name__ == "__main__":
    unittest.main()
