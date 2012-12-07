#! usr/bin/env python

import unittest

"""
http://programmingpraxis.com/2009/05/29/double-transposition-cipher/
UNFINISHED
"""

def compute_numeric_key(word):
	sorted_word = sorted(word)
	numkey = []

	for letter in word:
		occurence_index = sorted_word.index(letter)
		numkey.append(str(occurence_index + 1))
		sorted_word[occurence_index] += " "
	
	return "".join(numkey)

def grid_laydown(plaintext, keylen):
	grid = ["" for i in range(keylen)]
	i = 0
	limit = len(plaintext)
	
	while i < limit:
		grid[i % keylen] += plaintext[i]
		i += 1
	
	return grid

class FunctionsTest(unittest.TestCase):
	"""
	Test on varying casing.
	"""

	def test_compute_numeric_key(self):
		self.assertEqual("25134", compute_numeric_key("coach"))
	
	def test_grid_laydown(self):
		expected_output = ["pagi", "rmps", "omr", "gia", "rnx"]
		self.assertEqual(expected_output, grid_laydown("programmingpraxis", 5))

if __name__ == "__main__":
	unittest.main()
