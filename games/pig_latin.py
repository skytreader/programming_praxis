#! usr/bin/env python

"""
http://programmingpraxis.com/2009/06/02/pig-latin/

TODO: Test for varying cases within text.
"""

def eng2pigl_word(word):
	if word[0] in "aeiouAEIOU":
		return word + "way"
	else:
		return word[1:len(word)] + word[0] + "ay"

def translate(translation, text):
	all_words = text.split(" ")
	translated = list(map(translation, all_words))
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
