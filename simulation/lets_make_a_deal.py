#! /usr/bin/env python

import random
import sys

"""
http://programmingpraxis.com/2009/07/24/lets-make-a-deal/
UNFINISHED
"""

DOOR_COUNT = 3
GOAT = 'G'
CAR = 'C'

def get_door_config():
	doors = [GOAT for i in range(DOOR_COUNT)]
	doors[random.randint(0, 2)] = CAR
	return doors

def simulate_game(simulation_count):
	"""
	Always switch and check winning odds.

	TODO Make decision to switch or not configurable.
	"""
	success_count = 0

	for i in range(simulation_count):
		door_config = get_door_config()
		random_pick = random.randint(0, 2)
		
		if door_config[random_pick] == GOAT:
			success_count += 1
		# Else, you picked the car but since we always switch
		# you lose this time around.
	
	return success_count

if __name__ == "__main__":
	success = simulate_game(int(sys.argv[1]))
	print("Out of " + sys.argv[1] + " games, we won " + str(success) + " times.")
