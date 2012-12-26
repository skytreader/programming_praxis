#! /usr/bin/env python3

"""
http://programmingpraxis.com/2011/12/27/cheating-hangman/
UNFINISHED
"""

def get_similar(word_list, metric, limit = 0):
    """
    Returns a subset of word_list, at most size limit, of similar
    words, as defined by the function metric. The function metric
    takes in a word a returns True or False. If True, the word is
    included.

    If the limit is 0, we get as many as we can from word_list. 0
    is set by default.
    """
    similar = []

    for word in word_list:
        if metric(word):
            similar.append(word)

    return similar

def make_length_metric(length):
    return lambda x: len(x) == length

def make_fit_metric(outline):
    def fit(word):
        outlen = len(outline)

        if outlen != len(word):
            return False

        for i in range(outlen):
            if outline[i] != '_' and outline[i] != word[i]:
                return False
        
        return True

   return fit

class CheatingHangman(object):
    
    def __init__(self, max_tries, word_filename):
        self.__words = []

        with open(word_filename) as word_file:
            for line in word_file:
                self.__words.append(line)
        
        self.__current_words = []
        self.__game_state = ""
        self.__max_tries = max_tries

    @property
    def game_state(self):
        self.__game_state
    
    def new_game(self):
        self.__current_words = get_similar(self.__words, make_length_metric(random.randint(1, 10)))

    def guess(self, guess):
        pass
