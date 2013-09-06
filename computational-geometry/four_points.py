#! /usr/bin/env python3

import unittest

"""
http://programmingpraxis.com/2013/01/02/four-points-determine-a-square/
"""

def dist(p1, p2):
    """
    Takes in two tuples. Assume element 0 is x, element 1 is y.
    Returns (x1 - x2) ** 2 + (y1 - y2) ** 2
    """
    return ((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2)

def __get_distance_set(fixed, pointset):
    """
    Returns the distance of fixed point to each point in pointset. The return
    list is sorted.
    """
    distance_set = []

    for p in pointset:
        distance_set.append(dist(fixed, p))

    distance_set.sort()

    return distance_set

def is_square(points):
    """
    Checks if the given four points are squares.
    """
    if len(set(points)) != 4:
        return False
    # Pick the first point and get its distance to the three other points.
    p0_distances = __get_distance_set(points[0], (points[1], points[2],
      points[3]))
    # Pick the second point and get its distance to the three other points.
    p1_distances = __get_distance_set(points[1], (points[0], points[2],
      points[3]))
    
    return p0_distances == p1_distances and len(set(p0_distances)) == 2

class FunctionsTest(unittest.TestCase):
    
    def test_is_square(self):
        self.assertTrue(is_square(((0, 0), (0, 1), (1, 1), (1, 0))))
        self.assertTrue(is_square(((0, 0), (2, 1), (3, -1), (1, -2))))
        self.assertTrue(is_square(((0, 0), (1, 1), (0, 1), (1, 0))))

        self.assertFalse(is_square(((0, 0), (0, 2), (3, 2), (3, 0))))
        self.assertFalse(is_square(((0, 0), (3, 4), (8, 4), (5, 0))))
        self.assertFalse(is_square(((0, 0), (0, 0), (1, 0), (0, 1))))

        self.assertFalse(is_square(((0, 0), (0, 0), (0, 0), (0, 0))))

if __name__ == "__main__":
    unittest.main()
