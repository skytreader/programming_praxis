#! usr/bin/env python

import math

"""
http://programmingpraxis.com/2009/03/31/rail-fence-cipher/
"""

def encrypt(message, key):
	k = key
	origin = 0
	gap = 0
	encrypted = ""
	limit = len(message)
	gap_limit = (key - 1) * 2
	
	while k != 0:
		period = (k - 1) * 2
		
		if period == 0:
			period = (key - 1) * 2
		
		index = origin
		take_gap = False
		
		while index < limit:
			encrypted += message[index]
			
			if take_gap and gap != 0 and k != 1:
				index += gap * 2
			else:
				index += period
			
			take_gap = not take_gap
		
		origin += 1
		k -= 1
		gap += 1
	
	return encrypted

def str_insert(main_string, insert_string, index):
	listed = list(main_string)
	listed.insert(index, insert_string)
	return "".join(listed)

def decrypt(message, key):
	k = key
	msg_len = len(message)
	decrypted = ""
	
	while k != 0:
		period = (k - 1) * 2
		char_take = math.floor(msg_len / period)
		# need to know the "insert index"

if __name__ == "__main__":
	print(encrypt("PROGRAMMING PRAXIS", 4))
	print(encrypt("PROGRAMMING PRAXIS", 2))
