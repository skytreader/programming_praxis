#! /usr/bin/env python3

import math
import random

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
		self.elo_rating = elo_rating

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
	team_count = len(block)
	this_round = block

	while len(this_round) != 1:
		participants_remaining = len(this_round)
		skip_indices = range(participants_remaining)
		next_round = []
		for i in skip_indices:
			if i + 1 < participants_remaining:
				next_round.append(simulate_match(this_round[i], this_round[i + 1]))
			else:
				pass

		this_round = next_round
	
	return this_round[0]

if __name__ == "__main__":
	win_times = {"BRA":0, "ESP":0, "NED":0, "ARG":0, "ENG":0, "GER":0, "URU":0, "CHI":0, "POR":0, "MEX":0, "USA":0, "PAR":0, "KOR":0, "JPN":0, "GHA":0, "SVK":0}

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

	for i in range(1000000):
		# Create the competing teams.
		winner = simulate_block(tournament_block)
		win_times[winner.country_code] += 1
		print("Cup " + str(i + 1) + " winner is " + winner.country_code)

		# Reset ELOs
		brazil.elo_rating = 2082
		spain.elo_rating = 2061
		netherlands.elo_rating = 2045
		argentina.elo_rating = 1966
		england.elo_rating = 1945
		germany.elo_rating = 1930
		uruguay.elo_rating = 1890
		chile.elo_rating = 1883
		portugal.elo_rating = 1874
		mexico.elo_rating = 1873
		united_states.elo_rating = 1785
		paraguay.elo_rating = 1771
		korea.elo_rating = 1746
		japan.elo_rating = 1744
		ghana.elo_rating = 1711
		slovakia.elo_rating = 1654
	
	print(str(win_times))
