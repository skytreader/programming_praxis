#! /usr/bin/env python3

import random
import unittest

"""
http://programmingpraxis.com/2009/11/17/master-mind-part-1/
UNFINISHED
"""

class Setter(object):
	
	def __init__(self, code_size):
		self.__random_code = self.__generate_random_code(code_size)
	
	@property
	def random_code(self):
		return self.__random_code
	
	@random_code.setter
	def random_code(self, new_code):
		# TODO Check for the format of the string
		self.__random_code = new_code
	
	def regenerate_code(self, code_size):
		"""
		Regenerates the random code of this setter.
		"""
		self.__random_code = self.__generate_random_code(code_size)

	def __generate_random_code(self, size):
		"""
		Returns a random code of the specified length as a tuple. The code
		will be made up of random integers 0-9.
		"""
		return "".join([str(random.randint(0, 9)) for i in range(size)])
	
	def judge(self, answer):
		"""
		Returns a string comprised of 'B' and 'W'. 'B' means a correctly-placed
		symbol. 'W' means a symbol included in the code but in the wrong place
		in the answer.
		"""
		judgement = ""
		blacks = []

		# Accomplish by a two-stage pass: scan for the B's first and then the W's
		# next
		limit = len(self.__random_code)
		
		for i in range(limit):
			if answer[i] == self.__random_code[i]:
				judgement += 'B'
				blacks.append(i)
		
		for i in range(limit):
			if i not in blacks and answer[i] in self.__random_code:
				judgement += 'W'
		
		return judgement

def play(code_size):
	mastermind = Setter(code_size)
	solved_string = ''.join(['B' for i in range(code_size)])
	judgement = ''

	while judgement != solved_string:
		guess = input("guess> ")

		while len(guess) != code_size:
			print("Please enter a " + str(code_size) + "-digit string")
			guess = input("guess> ")
		
		judgement = mastermind.judge(guess)
		print(judgement)

class SetterTest(unittest.TestCase):
	
	def setUp(self):
		self.__setter = Setter(4)
	
	def test_judge(self):
		self.__setter.random_code = "1415"
		
		self.assertEqual(self.__setter.judge("9265"), 'B')
		self.assertEqual(self.__setter.judge("0000"), "")
		self.assertEqual(self.__setter.judge("3589"), 'W')
		self.assertEqual(self.__setter.judge("1415"), "BBBB")

if __name__ == "__main__":
	#unittest.main()
	play(4)
