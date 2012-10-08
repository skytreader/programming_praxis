#! usr/bin/env python

"""
http://programmingpraxis.com/2009/03/31/rail-fence-cipher/
"""

def encrypt(message, key):
	k = key
	origin = 0
	encrypted = ""
	limit = len(message)
	
	while k != 0:
		period = (k - 1) * 2
		index = origin
		
		while index < limit:
			encrypted += message[index]
			index += period
		
		origin += 1
	
	return encrypted

if __name__ == "__main__":
	print(encrypt("PROGRAMMING PRAXIS", 4))
