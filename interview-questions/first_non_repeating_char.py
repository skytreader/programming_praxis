#! /usr/bin/env python

import unittest

"""
http://programmingpraxis.com/2011/08/19/first-non-repeating-character/
"""

def first_non_repeating(s):
	"""
	NAIVE APPROACH!

	Returns the first letter which does not repeat later
	in the string. If there is no such letter, this function
	returns false.
	"""
	letter_index = 0
	limit = len(s)
	consumed = set()

	while letter_index < limit:
		if s[letter_index] not in s[letter_index + 1:limit] and s[letter_index] not in consumed:
			return s[letter_index]
		
		consumed.add(s[letter_index])
		letter_index += 1
	
	return False

class FunctionsTest(unittest.TestCase):
	
	def test_first_non_repeating(self):
		self.assertEqual(first_non_repeating("aabcbcdeef"), 'd')
		self.assertEqual(first_non_repeating("aabbccx"), 'x')
		self.assertFalse(first_non_repeating("aabbccxddx"))

if __name__ == "__main__":
	unittest.main()
