#! usr/bin/env python

import unittest

"""
http://programmingpraxis.com/2009/05/29/double-transposition-cipher/
UNFINISHED
"""

def compute_numeric_key(word):
	"""
	Computes the numeric key of the given string. The characters are
	sorted and then each character in the original word is replaced
	by it's position in the sorted sequence. If a letter is repeated,
	it's numeric replacement should be increasing left to right.

	This uses Python's sorted function to sort.

	Returns a numeric string.
	"""
	sorted_word = sorted(word)
	numkey = []

	for letter in word:
		occurence_index = sorted_word.index(letter)
		numkey.append(str(occurence_index + 1))
		sorted_word[occurence_index] += " "
	
	return "".join(numkey)

def grid_laydown(plaintext, keylen):
	"""
	Lays down the given plaintext in a grid based on the given key
	length. The text is laid-down left-to-right, top-to-bottom.

	Returns a list of strings. Each string is one column. The columns are
	arranged from left to right.
	"""
	grid = ["" for i in range(keylen)]
	i = 0
	limit = len(plaintext)
	
	while i < limit:
		grid[i % keylen] += plaintext[i]
		i += 1
	
	return grid

def encrypt(plaintext, key):
	numeric_key = compute_numeric_key(key)
	grid_cols = len(key)
	cipher_grid = grid_laydown(plaintext, grid_cols)
	encrypted_blocks = [None for i in range(grid_cols)]

	for i in range(grid_cols):
		encrypted_blocks[i] = cipher_grid[int(numeric_key.index(str(i + 1)))]
	
	return "".join(encrypted_blocks)

class FunctionsTest(unittest.TestCase):
	"""
	Test on varying casing.
	"""

	def test_compute_numeric_key(self):
		self.assertEqual("25134", compute_numeric_key("coach"))
	
	def test_grid_laydown(self):
		expected_output = ["pagi", "rmps", "omr", "gia", "rnx"]
		self.assertEqual(expected_output, grid_laydown("programmingpraxis", 5))
	
	def test_encrypt(self):
		self.assertEqual("omrpagigiarnxrmps", encrypt("programmingpraxis", "coach"))

if __name__ == "__main__":
	unittest.main()
