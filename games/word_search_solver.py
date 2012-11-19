#! usr/bin/env python

"""
http://programmingpraxis.com/2009/05/26/word-search-solver/
UNFINISHED
"""

def search_startswith(prefix, word_set):
	"""
	Returns a list of all the words in word_set that starts
	with the given prefix.
	"""
	all_starts = []
	
	for word in word_set:
		if word.startswith(prefix):
			all_starts.append(word)
	
	return all_starts

def get_neighbors(row, col):
	"""
	Returns a list of tuples, representing the neighbors of the given
	cell, as described by row and col.
	"""
	pass

def search(word_set, letter_block):
	"""
	Searches for all the words in word_set in letter_block. Returns
	a list of strings specifying the results of the search.
	
	word_set and letter_block is a list of strings. We assume that
	all the strings in letter_block have the same length.
	
	Test cases:
	 - w_n in word_set is a prefix of w_m in word_set.
	 - intersecting starts: the initial letter of one word in word_set
	   is found in the same cell as the initial letter of another word
	   in word_set.
	"""
	block_height = len(letter_block)
	block_width = len(letter_block[0])
	
	for row in range(block_height):
		for col in range(block_width):
			prefix = letter_block[row][col]
			
			prefix_matches = search_startswith(prefix, word_set)
			
			while prefix_matches:
				neighbors = get_neighbors(row, col)
				
				for letter_cell in neighbors:
					prefix += letter_block[letter_cell[0]][letter_cell[1]]
					prefix_matches = search_startswith(prefix, word_set)
