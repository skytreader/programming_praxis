#! usr/bin/env python

import re

"""
http://programmingpraxis.com/2009/06/02/pig-latin/

TODO: Test for varying cases within text.
TODO: Use regex for stripping!
"""

LOWER = "abcdefghijklmnopqrstuvwxyz"
UPPER = LOWER.upper()
ALPHABET = LOWER + UPPER

def eng2pigl_word(w):
	prefix_match = re.match(r"^([^a-zA-Z]*)([a-zA-Z]+)$", w)
	prefix = ""
	
	if prefix_match is None:
		word = w
	else:
		word = prefix_match.group(2)
		prefix = prefix_match.group(1)
	
	if word[0] in "aeiouAEIOU":
		return prefix + word + "way"
	else:
		return prefix + word[1:len(word)] + word[0] + "ay"

def strip_non_letter(word):
	match = re.match(r"^([a-zA-Z]+)([^a-zA-Z]*)$", word)
	puncs = ""
	stripped = ""
	
	if match is None:
		stripped = word
	else:
		stripped = match.group(1)
		puncs = match.group(2)
	
	return [stripped, puncs]

def translate(translation, text):
	"""
	This works assuming that all words are properly spaced and
	that all possible punctuation are found at the end of the
	word.
	"""
	all_words = text.split(" ")
	strip_parsing = list(map(strip_non_letter, all_words))
	get_words = list(map(lambda x: x[0], strip_parsing))
	capitals = list(map(lambda word: word[0] in UPPER, get_words))
	get_puncs = list(map(lambda x: x[1], strip_parsing))
	translated = list(map(translation, get_words))
	
	word_index = 0
	
	for punctuations in get_puncs:
		translated[word_index] += punctuations
		
		if capitals[word_index]:
			this_word = translated[word_index]
			translated[word_index] = this_word[0].upper() + this_word[1:len(this_word)].lower()
		
		word_index += 1
	
	return " ".join(translated)

def eng2pigl(text):
	"""
	Assuming plain text separated with spaces, no punctuation
	whatsoever.
	"""
	return translate(eng2pigl_word, text)

def pigl2eng_word(word):
	"""
	Idea: have a dictionary of english words which we can use
	to resolve translation abiguities. (Next time).
	"""
	sansay = word[0:len(word) - 2]
	last_char = sansay[len(sansay) - 1]
	sans_last_char = sansay[0:len(sansay) - 1]
	
	return last_char + sans_last_char

def pigl2eng(text):
	return translate(pigl2eng_word, text)

if __name__ == "__main__":
	print(eng2pigl("nix scram stupid art"))
	print(pigl2eng(eng2pigl("Pig Latin")))
	print(eng2pigl("I'm not at all disappointed Mycroft, Watson, and Lestrade... ~Sherlock Holmes."))
