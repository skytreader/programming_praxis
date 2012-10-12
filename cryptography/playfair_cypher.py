#! usr/bin/env python

PLAYFAIR_ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ";

def generate_key_square(key):
	"""
	Generates a 5-square for the given key. Returns
	a list of 5 strings, each containing 5 characters.
	"""
	key_square = []
	uniqued_key = ""
	
	for letter in key:
		if letter not in uniqued_key and letter != "J":
			uniqued_key += letter
	
	for letter in PLAYFAIR_ALPHABET:
		if letter not in uniqued_key:
			uniqued_key += letter
	
	square_size = 5
	bound_limit = 5
	max_limit = len(PLAYFAIR_ALPHABET)
	
	while bound_limit <= max_limit:
		key_square.append(uniqued_key[bound_limit - square_size:bound_limit])
		bound_limit += square_size
	
	return key_square

if __name__ == "__main__":
	print(generate_key_square("PLAYFAIR"))
