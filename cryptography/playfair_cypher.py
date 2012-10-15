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

def is_same_row(digram, key_square):
	"""
	Returns an iterable of iterables containing their positions
	in the key_square if they are in the same row. Otherwise,
	return False.
	"""
	row_index = 0
	
	for row in key_square:
		d1 = row.find(digram[0])
		d2 = row.find(digram[1])
		if d0 >= 0 and d1 >= 0:
			return ((row_index, d1), (row_index, d2))
		
		row_index += 1
	
	return False

def get_col(letter, key_square):
	"""Sure to return a good value"""
	for row in key_square:
		find = row.find(letter)
		if find >= 0:
			return find

def find_row(letter, key_square):
	"""Sure to return a good value"""
	limit = len(key_square)
	
	for i in range(limit):
		if letter in key_square[i]:
			return i

def is_same_col(digram, key_square):
	"""
	Returns an iterable of iterables containing their positions
	in the key_square if they are in the same col. Otherwise,
	return False.
	"""
	col1 = get_col(digram[0], key_square)
	col2 = get_col(digram[1], key_square)
	
	if col1 >= 0 and col2 >= 0 and col1 == col2:
		row1 = find_row(digram[0], key_square)
		row2 = find_row(digram[1], key_square)
		return ((row1, col1), (row2, col2))

def encipher(msg, key):
	pass

if __name__ == "__main__":
	print(generate_key_square("PLAYFAIR"))
	print(digrammify("PROGRAMMING PRAXIS"))
