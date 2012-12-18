#! usr/bin/env python3

import random

"""
http://programmingpraxis.com/2010/12/31/arithmetic-drill/

Not at all challenging! Maybe, next time, add some timers and levels.
"""

if __name__ == "__main__":
	while True:
		addend1 = random.randint(0, 9)
		addend2 = random.randint(0, 9)
		expected_sum = addend1 + addend2

		# Test for non numeric input
		answer = int(input(str(addend1) + " + " + str(addend2) + " = "))

		while answer != expected_sum:
			print("Wrong, try again!")
			answer = int(input(str(addend1) + " + " + str(addend2) + " = "))

		print("Right!")
