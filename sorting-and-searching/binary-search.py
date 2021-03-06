#! /usr/bin/env python

import math
import unittest

"""
http://programmingpraxis.com/2009/03/23/binary-search/

(Might also use this in other problems.)
"""

def binary_search(sorted_space, query):
	"""
	Returns the index of the query in the sorted space if it
	is present in the list. Otherwise, returns a negative value.

	We assume that the list is sorted in ascending order.
	"""
	low_limit = 0
	hi_limit = len(sorted_space)
	cur_node_index = math.floor((low_limit + hi_limit) / 2)
	visited_nodes = set()

	while True and cur_node_index not in visited_nodes:
		visited_nodes.add(cur_node_index)

		if sorted_space[cur_node_index] == query:
			return cur_node_index
		elif sorted_space[cur_node_index] < query:
			low_limit = cur_node_index
		else:
			hi_limit = cur_node_index

		cur_node_index = math.floor((low_limit + hi_limit) / 2)
	
	return -1

class FunctionsTest(unittest.TestCase):
	
	def test_binary_search(self):
		"""
		Test cases:
		even-length list positive result
		even-length list negative result
		odd-length list positive result
		odd-length list negative result
		"""
		pi_list = [1,4,1,5,9,9,6,5,3,5,8,9,7,9,3,2,3,5,4,6,2,6,4,3,3,8,3,2,7,9,5,0,2,8,8,4,1,9,7,1,6,9]
		pi_list.sort()
		
		for i in range(10):
			positive_even = binary_search(pi_list, i)
			self.assertTrue(positive_even >= 0)
			self.assertEqual(pi_list[positive_even], i)
		
		negative_even = binary_search(pi_list, 42)
		self.assertEqual(negative_even, -1)

		odd_list = pi_list[0:len(pi_list) - 1]
		positive_odd = binary_search(odd_list, 5)
		self.assertTrue(positive_odd > 0)
		self.assertEqual(odd_list[positive_odd], 5)

		negative_odd = binary_search(odd_list, 34)
		self.assertEqual(negative_odd, -1)

if __name__ == "__main__":
	unittest.main()
