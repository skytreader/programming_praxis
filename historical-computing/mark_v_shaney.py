#! usr/bin/env python

import unittest
import random
import sys

"""
http://programmingpraxis.com/2009/02/27/mark-v-shaney/
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
	For now, let's consider each line separately. And consider
	paragraphs and stuff.
	"""
	# TODO Use a more efficient data structure to store the table.
	triple_table = []
	
	with open(text_filename) as training_text:
		for line in training_text:
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
			random_index = get_starting_index(text_triples)
			random_triple = text_triples[random_index]
			last_word = random_triple[2]
			random_text = " ".join(random_triple[0:2])
		else:
			continuing_triples = list(filter(lambda triple: triple[0] == last_word, text_triples))
			triples_count = len(continuing_triples)
			
			if triples_count == 0:
				break
			
			random_triple = continuing_triples[random.randint(0, triples_count - 1)]
			for_joining = random_text.split(" ")
			for_joining.extend(random_triple[0:2])
			last_word = random_triple[2]
			random_text = " ".join(for_joining)
		
		i += 1
	
	return random_text

def get_starting_index(triples):
	"""
	Gets a random index within the given triples list with the additional constraint
	that the first element of that triple starts with a capital letter.
	"""
	caps_starters = list(filter(lambda triple: triple[0][0].isupper(), triples))
	starter_count = len(caps_starters)
	random_triple = caps_starters[random.randint(0, starter_count - 1)]
	return triples.index(random_triple)

class FunctionsTest(unittest.TestCase):
	
	def test_save_triples(self):
		long_sentence = save_triples("the quick brown fox jumps over the lazy dog.")
		self.assertEqual(long_sentence, [('the', 'quick', 'brown'), ('quick', 'brown', 'fox'), ('brown', 'fox', 'jumps'), ('fox', 'jumps', 'over'), ('jumps', 'over', 'the'), ('over', 'the', 'lazy'), ('the', 'lazy', 'dog.')])
		
		short_sentence = save_triples("the quick brown")
		self.assertEqual(short_sentence, [('the', 'quick', 'brown')])
		
		shorter_sentence = save_triples("the quick")
		self.assertEqual(shorter_sentence, [])
	
	def test_get_starting_index(self):
		triple_list = [('Someone', 'you', 'me'), ('me', 'Someone', 'no'), ('me', 'no', 'Evil'), ('no', 'caps', 'really'), ('Menu', 'source', 'engine')]
		test_metric = lambda x: x == 0 or x == 4

		for i in range(100):
			self.assertTrue(test_metric(get_starting_index(triple_list)))

if __name__ == "__main__":
	#unittest.main()
	if len(sys.argv) != 3:
		print("Expecting 2 arguments: the filename of the training text and the number of iterations.")
		sys.exit()
	triples = train_on_text(sys.argv[1])
	random_problem = generate_random_text(triples, int(sys.argv[2]))
	print(random_problem)
