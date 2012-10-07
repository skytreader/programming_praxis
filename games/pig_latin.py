#! usr/bin/env python

"""
http://programmingpraxis.com/2009/06/02/pig-latin/
"""

def eng2pigl_word(word):
	if word[0] in "aeiouAEIOU":
		return word + "way"
	else:
		return word[1:len(word)] + word[0] + "ay"

def eng2pigl(text):
	"""
	Assuming plain text separated with spaces, no punctuation
	whatsoever.
	"""
	all_words = text.split(" ")
	pigled = list(map(eng2pigl_word, all_words))
	return " ".join(pigled)

if __name__ == "__main__":
	print(eng2pigl("nix scram stupid art"))
