#! /usr/bin/env python3

from string import ascii_letters
import unittest

"""
https://programmingpraxis.com/2016/02/16/finding-god/
"""

def convert_to_letter_counts(line):
    letter_filter = lambda word: "".join(list(filter(lambda c: c in ascii_letters, word)))
    space_parse = line.split()
    letter_nodes = list(map(letter_filter, space_parse))
    return list(map(len, letter_nodes))

def link_nodes(num_nodes):
    """
    num_nodes - a list of lists, each list not necessarily of the same length,
    that must be linked.
    """
    pass

class FunctionsTest(unittest.TestCase):
    
    def test_convert_to_letter_counts(self):
        spam = "In the beginning God created the heaven and the earth."
        spam_lc = [2, 3, 9, 3, 7, 3, 6, 3, 3, 5]
        self.assertEqual(spam_lc, convert_to_letter_counts(spam))

if __name__ == "__main__":
    unittest.main()
