#! usr/bin/env python

"""
http://programmingpraxis.com/contents/themes/
"""

THRESHOLD = 0.000001

def bisection(x):
	lower_limit = 1
	upper_limit = x
	prev_midpoint = 0
	midpoint = (upper_limit - lower_limit + 1) / 2
	candidate_square = midpoint ** 2
	
	while abs(candidate_square - x) > THRESHOLD and \
			prev_midpoint != midpoint:
		if candidate_square > x:
			upper_limit = midpoint
		else:
			lower_limit = midpoint
		
		prev_midpoint = midpoint
		midpoint = ((upper_limit - lower_limit + 1) / 2) + lower_limit
		candidate_square = midpoint ** 2
	
	return midpoint

def hero(x):
	lower_limit = 1
	upper_limit = x
	prev_cand_root = 0
	candidate_root = (upper_limit - lower_limit + 1) / 2
	candidate_square = candidate_root ** 2
	
	while abs(candidate_square - x) > THRESHOLD and \
			prev_cand_root != candidate_root:
		if candidate_square > x:
			upper_limit = candidate_root
		else:
			lower_limit = candidate_root
		
		print(" ".join(list(map(str, [lower_limit, upper_limit, candidate_root]))))
		
		prev_cand_root = candidate_root
		candidate_root = (x + (x / candidate_root)) / 2
		candidate_square = candidate_root ** 2
	
	return candidate_root

if __name__ == "__main__":
	tests = [4, 16, 23, 40, 2, 167]
	print("THRESHOLD: " + str(THRESHOLD))
	print("==========BISECTION==========")
	for test_case in tests:
		print("sqrt(" + str(test_case) + ") = " + str(bisection(test_case)))
	print("==========HERO'S==========")
	for test_case in tests:
		print("sqrt(" + str(test_case) + ") = " + str(hero(test_case)))
