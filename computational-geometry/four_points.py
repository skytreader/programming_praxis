#! /usr/bin/env python3

import unittest

"""
http://programmingpraxis.com/2013/01/02/four-points-determine-a-square/
UNFINISHED
"""

def dist(p1, p2):
    """
    Takes in two tuples. Assume element 0 is x, element 1 is y.
    Returns (x1 - x2) ** 2 + (y1 - y2) ** 2
    """
    return ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)

def is_within_tolerance(v1, v2, tolerance = 0.0001):
    return abs(v1 - v2) <= tolerance

def __has_same_tolerance(p1, vs):
    for v in vs:
        if is_within_tolerance(p1, v):
            return True

    return False

def __possible_square_corner(p1, other_points):
    """
    Consider only the first three elements of other_points. Return true if at
    least two points in other_points have the same distance from p1.
    """
    similar = 0
    prevvals = []

    for i in range(4):
        d = dist(p1, other_points[i])
        if __has_same_tolerance(d, prevvals):
            similar += 1
        else:
            prevvals.append(d)
    
    return similar == 1

def is_square(points):
    """
    Checks if the given four points are squares.
    """
    for p in points:
        if not __possible_square_corner(p, points):
            return False

    return True

class FunctionsTest(unittest.TestCase):
    
    def test_is_square(self):
        self.assertTrue(is_square(((0, 0), (0, 1), (1, 1), (1, 0))))
        self.assertTrue(is_square(((0, 0), (2, 1), (3, -1), (1, -2))))
        self.assertTrue(is_square(((0, 0), (1, 1), (0, 1), (1, 0))))

if __name__ == "__main__":
    unittest.main()
