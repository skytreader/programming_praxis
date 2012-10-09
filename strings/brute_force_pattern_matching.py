#! usr/bin/env python

"""
http://programmingpraxis.com/2009/08/21/string-search-brute-force/
"""

def match_pattern(string_space, search_string):
	space_index = 0
	space_limit = len(string_space)
	
	while space_index < space_limit:
		space_runner = space_index
		pattern_found = True
		
		for character in search_string:
			if space_runner >= space_limit or \
			character != string_space[space_runner]:
				pattern_found = False
				break
			
			space_runner += 1
		
		if pattern_found:
			return space_index
		
		space_index += 1
	
	return -1

if __name__ == "__main__":
	print(match_pattern("looking", "king"))
	print(match_pattern("login", "log"))
	print(match_pattern("deoxyribonucleic acid", "xkcd"))
	print(match_pattern("firefighter", "fight"))
