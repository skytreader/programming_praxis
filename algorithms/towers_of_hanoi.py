#! /usr/bin/env python3

import sys

"""
http://programmingpraxis.com/2011/10/11/tower-of-hanoi/

(Though, contrary to Programming Praxis, I'm doing the iterative version.)
"""

def move_smallest_disk(disk_count, smallest_disk_index):
	"""Returns the new index of the smallest disk"""

	if not disk_count % 2:
		new_index = smallest_disk_index + 1
		new_index %= 3
	else:
		new_index = smallest_disk_index - 1 if smallest_disk_index != 0 else 2
	
	print("Move the smallest disk from peg " + str(smallest_disk_index) + " to peg " + str(new_index))
	return new_index

def make_legal_move(disks, diskcounts):
	"""
	disks is the disk size at the top of each peg
	Returns the new configuration of the game
	"""
	# Get the smallest disk after disk size 1
	smallest = lambda x: x != 0 and x != 1
	smallest = min(list(filter(smallest, disks)))
	smallest_index = disks.index(smallest)
	one_index = disks.index(1)

	legal_peg = list(filter(lambda x: x != smallest_index and x!= one_index, range(3)))[0]

	print("Move disk size " + str(smallest) + " from peg " + str(smallest_index + 1) + " to peg " + str(legal_peg + 1))
	
	diskcounts[legal_peg] += 1
	diskcounts[smallest_index] -= 1

	disks[legal_peg] = disks[smallest_index]
	disks[smallest_index] += 1 if diskcounts[smallest_index] else -disks[smallest_index]

def solve_puzzle(size):
	tower_states = [1, 0, 0]
	diskcounts = [size, 0, 0]
	smallest_disk_turn = True

	while tower_states != [0, 0, 1]:
		if smallest_disk_turn:
			small_index = tower_states.index(1)
			smallest_move = move_smallest_disk(size, small_index)
			
			tower_states[smallest_move] = 1
			tower_states[small_index] = 0 if diskcounts[small_index] == 1 else tower_states[small_index] + 1
			diskcounts[smallest_move] += 1
			diskcounts[small_index] -= 1
			
			if tower_states[small_index] > size:
				print("Ooops! Algo error!")
				exit()
		else:
			make_legal_move(tower_states, diskcounts)

		smallest_disk_turn = not smallest_disk_turn

if __name__ == "__main__":
	solve_puzzle(3)
