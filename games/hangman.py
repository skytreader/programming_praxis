#! usr/bin/env python

import random

"""
http://programmingpraxis.com/2011/12/20/hangman/

Assumptions:
	- All letters are in lowercase.
	- Alphabet is the set of (lowercase) alphanumeric characters plus
	  the single whitespace character.
"""

WORD_LIST = ["computer science", "data structures and algorithms", "watercolor", "sketch"]

class Hangman(object):
	
	def __init__(self, word_list, max_tries = 6):
		self.word_list = word_list
		self.current_word = ""
		self.game_state = ""
		self.max_tries = max_tries
	
	def new_game(self):
		self.current_word = self.word_list[random.randint(0, len(self.word_list) - 1)]
		self.game_state = self.__blankify(self.current_word)
		self.try_count = 0
	
	def __blankify(self, word):
		blanked = ""
		
		for character in word:
			if character != " ":
				blanked += "_"
			else:
				blanked += " "
		
		return blanked
	
	def make_guess(self, letter_guess):
		"""
		Allows the player to make a guess, changing the game
		state depending on whether the guess is right or wrong.
		"""
		is_guess_correct = False
		letter_index = 0
		game_state_list = list(self.game_state)
		
		if self.try_count >= self.max_tries:
			return
		
		for character in self.current_word:
			if character == letter_guess and \
					game_state_list[letter_index] == "_":
				game_state_list[letter_index] = letter_guess
				is_guess_correct = True
			
			letter_index += 1
		
		self.game_state = "".join(game_state_list)
		
		if not is_guess_correct:
			self.try_count += 1
	
	def has_won(self):
		for letter in self.game_state:
			if letter == "_":
				return False
		
		return True
	
if __name__ == "__main__":
	game_instance = Hangman(WORD_LIST)
	
	while True:
		game_instance.new_game()
		
		while game_instance.try_count < game_instance.max_tries:
			print(game_instance.game_state)
			game_instance.make_guess(input("Make a guess: "))
			
			if game_instance.has_won():
				print(game_instance.game_state)
				print("Congratulations!")
				break
		
		if not game_instance.has_won():
			print("Sorry. The word is '" + game_instance.current_word + "'")
