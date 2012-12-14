#! /usr/bin/env python

import math
import random

from ../dry/dataset_reader import DataSetReader

"""
http://programmingpraxis.com/2010/06/29/world-cup-prognostication/
UNFINISHED
"""

class Team(object):
	
	def __init__(self, country_code, elo_rating):
		self.country_code = country_code
		self.elo_rating = self.elo_rating

def compute_new_elo(team_A, team_B, game_weight, goal_difference, win_loss):
	"""
	Takes in an instance of team and computes the team A's new ELO for
	a game with team_B as an opponent, given game weight, goal differential,
	win/loss. Modifies the elo_rating of team_A in the process.
	"""
	winning_expectation = compute_winning_expectation(team_A, team_B) 
	team_A.elo_rating += (game_weight * goal_difference * (win_loss - winning_expectation))

def compute_winning_expectation(team_A, team_B):
	return 1 / (1 + 10 ** ((team_B.elo_rating - team_A.elo_rating) / 400))

def simulate_match(team_A, team_B):
	"""
	Simulates a match between team_A and team_B, through their
	ELO rating. The ELO rating is recalculated for both teams
	assuming a goal difference of 1. Returns the team (with updated
	ELO rating) that won the match.
	"""
	win_A = compute_winning_expectation(team_A, team_B)
	win_B = compute_winning_expectation(team_B, team_A)
	match_determinant = random.random()
	better_elo = max(win_A, win_B)
	
	if better_elo == win_A:
		better_team = team_A
	else:
		better_team = team_B
	
	if match_determinant <= better_elo:
		compute_new_elo(team_A, team_B, 60, 1, 1)
		compute_new_elo(team_B, team_A, 60, 1, 0)
	else:
		compute_new_elo(team_A, team_B, 60, 1, 0)
		compute_new_elo(team_B, team_A, 60, 1, 1)
	
	return better_team

def package_binary_tree(teams):
	"""
	Given a list of teams where adjacent (even, odd) indices
	are opponents for roud one, create a binary tree to
	represent the whole tournament.

	We assume zero-indexing.
	"""
	level_count = math.floor(math.log(len(teams), 2))

def simulate_block(block):
	"""
	block is a list which we take to be a complete binary
	tree (since the structure of a tournament is actually
	a complete binary tree).

	Initially, only the bottom-most row of the binary tree
	is filled. As teams win, they "float up" the tree until
	one reaches the root ("the winner").
	"""
	pass
