#! usr/bin/env python

import unittest
import random

"""
http://programmingpraxis.com/2009/02/27/mark-v-shaney/
UNFINISHED
"""

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
	# TODO Use a more efficient data structure to store the table.
	triple_table = []
	
	with open(text_filename) as training_text:
		for line in text_filename:
			triple_table.extend(save_triples(line))
	
	return triple_table

def generate_random_text(text_triples, text_limit):
	"""
	Generate random text based on the given text_triples. The iteration
	will run for the given text_limit.
	"""
	random_text = ""
	last_word = ""
	i = 0
	
	while i < text_limit:
		if last_word == "":
			triples_count = len(text_triples)
			random_triple = text_triples[random.randint(0, triples_count)]
			last_word = random_triple[1]
			random_text = " ".join(random_triple)
		else:
			continuing_triple = list(filter(lambda triple: triple[1] == last_word, text_triples))
			triples_count = len(continuing_triples)
			random_triple = text_triples[random.randint(0, triples_count)]
			random_text = " ".join(random_text.split(" ").extend(random_triple))
		
		i += 1
	
	return random_text

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
