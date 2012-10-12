#! usr/bin/env python

PLAYFAIR_ALPHABET = "ABCDEFGHIKLMNOPQRSTUVWXYZ";

"""
Super assumption: all letters in the strings to be processed
are in CAPITALS.
"""

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

def digrammify(msg):
	"""
	Breaks msg into chunks of two characters each. If, in a chunk,
	a letter repeats, we only take one letter and, for that chunk,
	replace the next letter with an 'X'. The ommitted letter will
	appear in the next chunk. We also append an 'X' if there is
	less than two characters left for the last chunk.
	
	digrammify ignores spaces.
	
	@return A list of strings, each only two characters each.
	"""
	digram_chunks = []
	# Strip spaces
	msg = msg.replace(" ", "")
	# Change all "J" to "I"
	msg = msg.replace("J", "I")
	
	digram_size = 2
	bound_limit = 2
	max_limit = len(msg)
	
	while bound_limit <= max_limit:
		# FIXME Ignore repeating letters in a chunk for now.
		candidate = msg[bound_limit - digram_size:bound_limit]
		
		if candidate[0] == candidate[1]:
			digram_chunks.append(candidate[0] + "X")
			bound_limit += 1
		else:
			digram_chunks.append(msg[bound_limit - digram_size:bound_limit])
			bound_limit += digram_size
	
	return digram_chunks

if __name__ == "__main__":
	print(generate_key_square("PLAYFAIR"))
	print(digrammify("PROGRAMMING PRAXIS"))
