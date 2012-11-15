#! usr/bin/env python

import unittest

"""
http://programmingpraxis.com/2009/02/27/mark-v-shaney/
UNFINISHED
"""

# TODO Use a more efficient data structure to store the table.
triple_table = []

def save_triples(line):
	"""
	Gets all the adjacent triples in a line and returns them
	as a list of tuples. The possible words in the line should
	be space-separated. If the line has less than three words,
	return an empty list. If the line has exactly three words,
	that should be considered as a tuple in itself.
	"""
	line_parse = line.split(" ")
	limit = len(line_parse) - 3
	i = 0
	triples = []
	
	while i <=	 limit:
		triple_item = (line_parse[i], line_parse[i + 1], line_parse[i + 2])
		triples.append(triple_item)
		i += 1
	
	return triples

def train_on_text(text_filename):
	"""
	For now, let consider each line separately. And consider
	paragraphs and stuff.
	"""
	with open(text_filename) as training_text:
		for line in text_filename:
			triple_table.extend(save_triples(line))

def generate_markov_probability():
	

class FunctionsTest(unittest.TestCase):
	
	def test_save_triples(self):
		long_sentence = save_triples("the quick brown fox jumps over the lazy dog.")
		self.assertEqual(long_sentence, [('the', 'quick', 'brown'), ('quick', 'brown', 'fox'), ('brown', 'fox', 'jumps'), ('fox', 'jumps', 'over'), ('jumps', 'over', 'the'), ('over', 'the', 'lazy'), ('the', 'lazy', 'dog.')])
		
		short_sentence = save_triples("the quick brown")
		self.assertEqual(short_sentence, [('the', 'quick', 'brown')])
		
		shorter_sentence = save_triples("the quick")
		self.assertEqual(shorter_sentence, [])

if __name__ == "__main__":
	unittest.main()
