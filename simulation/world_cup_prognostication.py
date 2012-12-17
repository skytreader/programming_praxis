#! /usr/bin/env python3

import math
import random

from ../dry/dataset_reader import DataSetReader

"""
http://programmingpraxis.com/2010/06/29/world-cup-prognostication/
UNFINISHED

Test cases:
 - Even number of teams
 - Odd number of teams
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

def simulate_block(block):
	"""
	block is a list of teams. A team at an even-numbered index n
	contests with the team at odd-numbered index n + 1. This
	method returns the overall winner of the whole block.

	Note that a whole tournament may be represented as one
	big block.
	"""
	team_count = len(teams)
	this_round = teams

	while len(this_round) != 1:
		skip_indices = range(len(this_round))
		next_round = []
		for i in skip_indices:
			if i + 1 < team_count:
				pass
			else:
				next_round.append(simulate_match(this_round[i], this_round[i + 1]))

		this_round = next_round
	
	return this_round[0]

if __name__ == "__main__":
	# Create the competing teams.
	brazil = Team("BRA", 2082)
	spain = Team("ESP", 2061)
	netherlands = Team("NED", 2045)
	argentina = Team("ARG", 1966)
	england = Team("ENG", 1945)
	germany = Team("GER", 1930)
	uruguay = Team("URU", 1890)
	chile = Team("CHI", 1883)
	portugal = Team("POR", 1874)
	mexico = Team("MEX", 1873)
	united_states = Team("USA", 1785)
	paraguay = Team("PAR", 1771)
	korea = Team("KOR", 1746)
	japan = Team("JPN", 1744)
	ghana = Team("GHA", 1711)
	slovakia = Team("SVK", 1654)

	tournament_block = [uruguay, korea, united_states, ghana, netherlands, slovakia, brazil, chile, argentina, mexico, germany, england, paraguay, japan, spain, portugal]
	winner = simulate_block(tournament_block)
	print("The winner is " + winner.country_code)
