#! /usr/bin/env python3

import sys

"""
http://programmingpraxis.com/2009/04/10/anagrams/
"""

def is_anagrams(word1, word2):
	return get_char_count(word1) == get_char_count(word2)

def get_char_count(word):
	char_count = {}
	for letter in word:
		char_count[letter] = 1 if letter not in char_count.keys() else char_count[letter] + 1
	
	return char_count

def get_anagrams(ref_word, dict_filename):
	anagrams = []
	with open(dict_filename) as dictionary:
		for line in dictionary:
			line = line[0:len(line) - 1].lower()
			if is_anagrams(line, ref_word):
				anagrams.append(line)
	
	return anagrams

if __name__ == "__main__":
	print(str(get_anagrams(sys.argv[1].lower(), sys.argv[2])))
