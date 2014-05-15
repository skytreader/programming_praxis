#! /usr/bin/env python3

"""
http://programmingpraxis.com/2009/02/20/rot13/
"""

ALPHABET = "abcdefghijklmnopqrstuvwxyz"

def rot13(msg):
	transformed = ""
	lowered = msg.lower()
	str_index = 0
	
	for letter in lowered:
		if letter in ALPHABET:
			letter_index = ALPHABET.index(letter)
			transposed = (letter_index + 13) % len(ALPHABET)
			
			if letter != msg[str_index]:
				transformed = "".join([transformed, ALPHABET[transposed].upper()])
			else:
				transformed = "".join([transformed, ALPHABET[transposed]])
		else:
			transformed = "".join([transformed, letter])
	
	return transformed

if __name__ == "__main__":
	print(rot13("The butler did it!"))
	print(rot13("Gur ohgyre qvq vg!"))
	print(rot13("Cebtenzzvat Cenkvf vf sha!"))
