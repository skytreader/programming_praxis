#! usr/bin/env python

import math

"""
http://programmingpraxis.com/2009/06/30/steve-yegges-phone-screen-coding-exercises/
"""

def reverse_string(s):
	srev = ""
	
	for character in s:
		srev = character + srev
	
	return srev

def fib(n):
	f0 = 1
	f1 = 1
	
	if n == 0 or n == 1:
		return f1
	else:
		for i in range(n):
			f0, f1 = f1, f1 + f0
		
		return f1

def mul_table(n, m):
	"""
	Prints out an n x m multiplication table because hard-
	coded constraints are not challenging at all.
	"""
	table = ""
	maxlen = len(str(n * m))
	format_string = "{0:" + str(maxlen) + "} "
	
	for i in range(n):
		i += 1
		for j in range(m):
			j += 1
			table += format_string.format(str(i * j))
		
		table += "\n"
	
	return table

def text_file_summation(filename):
	summation = 0
	
	with open(filename, "r") as int_file:
		for int_line in int_file:
			summation += int(int_line)
	
	return summation

def odd_summation(lower_limit, upper_limit):
	summation = 0
	
	while lower_limit <= upper_limit:
		if (lower_limit % 2):
			summation += lower_limit
		
		lower_limit += 1
	
	return summation

def largest_int(intlist):
	max_val = float("-inf")
	
	for i in intlist:
		if i > max_val:
			max_val = i
	
	return max_val

def to_hex(dec):
	hex_alphabet = "0123456789abcdef"
	hexstring = ""
	
	while dec >= 0:
		hexstring += hex_alphabet[dec % 16]
		dec = math.floor(dec / 16)
		
		if dec == 0:
			break
	
	return hexstring

def to_hex_string(r, g, b):
	return "".join([to_hex(r), to_hex(g), to_hex(b)])

if __name__ == "__main__":
	print("==========String reversal============")
	print(reverse_string("steve yegge"))
	
	print("==========Fibonacci============")
	for i in range(10):
		print(fib(i))
	
	print("==========12x12 multiplication table============")
	print(mul_table(12, 12))
	
	print("==========Text file summation============")
	print(text_file_summation("intfile.txt"))
	
	print("==========Odd summation============")
	print(odd_summation(1, 99))
	
	print("==========Largest int============")
	print(largest_int([0, 1, 2, 3, 4, 5, 2, 3]))
	
	print("==========Hex conversion============")
	print(to_hex_string(255, 255, 255))
	print(to_hex_string(0, 0, 0))
	print(to_hex_string(254, 54, 33))
