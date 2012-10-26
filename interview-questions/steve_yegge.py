#! usr/bin/env python

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
	pass

def odd_summation(lower_limit, upper_limit):
	summation = 0
	
	while lower_limit <= upper_limit:
		if (lower_limit % 2):
			summation += lower_limit
		
		lower_limit += 1
	
	return summation

if __name__ == "__main__":
	print("==========String reversal============")
	print(reverse_string("steve yegge"))
	
	print("==========Fibonacci============")
	for i in range(10):
		print(fib(i))
	
	print("==========12x12 multiplication table============")
	print(mul_table(12, 12))
	
	print("==========Text file summation============")
	print("not implemented yet")
	
	print("==========Odd summation============")
	print(odd_summation(1, 99))
