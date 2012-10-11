#! usr/bin/env python

import math

"""
http://programmingpraxis.com/2009/03/31/rail-fence-cipher/
"""

def encrypt(message, key):
	encrypted = ""
	seq = rail_fence_sequence(len(message), key)
	
	for seq_no in seq:
		encrypted += message[seq_no]
		
	return encrypted

def rail_fence_sequence(msg_len, key):
	k = key
	origin = 0
	gap = 0
	gap_limit = (key - 1) * 2
	sequence = []
	
	while k != 0:
		period = (k - 1) * 2
		
		if period == 0:
			period = (key - 1) * 2
		
		index = origin
		take_gap = False
		
		while index < msg_len:
			sequence.append(index)
			
			if take_gap and gap != 0 and k != 1:
				index += gap * 2
			else:
				index += period
			
			take_gap = not take_gap
		
		origin += 1
		k -= 1
		gap += 1
	
	return sequence

def decrypt(message, key):
	msg_len = len(message)
	decrypted = ['' for i in range(msg_len)]
	seq = rail_fence_sequence(msg_len, key)
	index_runner = 0
	
	for letter in message:
		decrypted[seq[index_runner]] = letter
		index_runner += 1
	
	return "".join(decrypted)

if __name__ == "__main__":
	print(encrypt("PROGRAMMING PRAXIS", 4))
	print(encrypt("PROGRAMMING PRAXIS", 2))
	print(decrypt("PMPRAM RSORIGAIGNX", 4))
	print(decrypt("PORMIGPAIRGAMN RXS", 2))
