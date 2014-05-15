#! /usr/bin/env python3

"""
http://programmingpraxis.com/2009/02/20/rot13/
"""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def ceasar(msg, shift):
	transformed = ""
	lowered = msg.lower()
	str_index = 0
	
	for letter in lowered:
		if letter in ALPHABET:
			letter_index = ALPHABET.index(letter)
			transposed = (letter_index + shift) % len(ALPHABET)
			
			if letter != msg[str_index]:
				transformed = "".join([transformed, ALPHABET[transposed].upper()])
			else:
				transformed = "".join([transformed, ALPHABET[transposed]])
		else:
			transformed = "".join([transformed, letter])
	
	return transformed

if __name__ == "__main__":
    print(ceasar("PROGRAMMINGPRAXIS", 3))
