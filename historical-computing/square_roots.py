#! usr/bin/env python

"""
http://programmingpraxis.com/contents/themes/
"""

THRESHOLD = 0.000001

def within_threshold(val):
	return val <= THRESHOLD

def bisection(x):
	lower_limit = 1
	upper_limit = x
	prev_midpoint = 0
	midpoint = (upper_limit + lower_limit) / 2
	candidate_square = midpoint ** 2
	
	while not within_threshold(abs(candidate_square - x)) and \
			not within_threshold(abs(prev_midpoint - midpoint)):
		if candidate_square > x:
			upper_limit = midpoint
		else:
			lower_limit = midpoint
		
		prev_midpoint = midpoint
		midpoint = ((upper_limit + lower_limit) / 2)
		candidate_square = midpoint ** 2
	
	return midpoint

def hero(x, initial_candidate = None):
	lower_limit = 1
	upper_limit = x
	prev_cand_root = 0
	candidate_root = (upper_limit + lower_limit) / 2
	candidate_square = candidate_root ** 2
	
	while not within_threshold(abs(candidate_square - x)) and \
			not within_threshold(abs(candidate_root - prev_cand_root)):
		if candidate_square > x:
			upper_limit = candidate_root
		else:
			lower_limit = candidate_root
		
		prev_cand_root = candidate_root
		candidate_root = (candidate_root + (x / candidate_root)) / 2
		candidate_square = candidate_root ** 2
	
	return candidate_root

if __name__ == "__main__":
	tests = [4, 5, 16, 23, 40, 2, 167, 125348]
	print("THRESHOLD: " + str(THRESHOLD))
	print("==========BISECTION==========")
	for test_case in tests:
		print("sqrt(" + str(test_case) + ") = " + str(bisection(test_case)))
	print("==========HERO'S==========")
	for test_case in tests:
		print("sqrt(" + str(test_case) + ") = " + str(hero(test_case)))
