#! /usr/bin/env python

import unittest

"""
http://programmingpraxis.com/2011/07/19/sum-of-two-integers/
"""

def will_sum_up_to(number_list, target_number):
	"""
	Thanks to Python's dynamic typing, this function is actually
	NOT constrained to integers, although it may not be very
	accurate given floating point inputs due to floating point
	handling issues.
	"""
	
	for number in number_list:
		remains = target_number - number
		
		# optimization: can use binary search here since order does not matter
		if remains in number_list:
			return True
	
	return False

class FunctionsTest(unittest.TestCase):
	
	def test_will_sum_up_to(self):
		self.assertTrue(will_sum_up_to([5, 5, 2, 1, 3, 3, 43, 23, 1, 24, 10], 10))
		self.assertFalse(will_sum_up_to([10, 20, 30], 10))
		self.assertTrue(will_sum_up_to([1,5,42,1,0,2,34,6,7], 1))

if __name__ == "__main__":
	unittest.main()
