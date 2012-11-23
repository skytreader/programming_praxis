#! /usr/bin/env python

import unittest

"""
http://programmingpraxis.com/2010/11/23/string-subsets/
"""

ALL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def get_letter_counts(s):
	"""
	Returns a dictionary with letters for keys and occurrence
	tallies for values.
	"""
	counts = {}

	for letter in ALL_LETTERS:
		counts[letter] = 0
	
	for letter in s:
		if letter in ALL_LETTERS:
			counts[letter] += 1
	
	return counts

def is_string_subset(s1, s2):
	"""
	Determines if string s2 is a subset of s1.
	"""
	counts1 = get_letter_counts(s1)
	counts2 = get_letter_counts(s2)
	s2_letters = counts2.keys()

	for letter in s2:
		if counts2[letter] != counts1[letter]:
			return False
	
	return True

class FunctionsTest(unittest.TestCase):
	
	def test_is_string_subset(self):
		self.assertTrue(is_string_subset("ABCD", "DA"))
		self.assertFalse(is_string_subset("ABCD", "DAD"))
		self.assertTrue(is_string_subset("ABCD", "DBCA"))

if __name__ == "__main__":
	unittest.main()
