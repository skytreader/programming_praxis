#! /usr/bin/env

import unittest

def remove_duplicates(s):
    encountered = []
    duplicates_removed = ""

    for character in s:
        if character not in encountered:
            duplicates_removed += character
            encountered.append(character)

    return duplicates_removed

def replace_runs_of_space(s):
    return " ".join(s.split())

class FunctionsTest(unittest.TestCase):
    
    def test_remove_duplicates(self):
        self.assertEqual("ab", remove_duplicates("aaabbb"))
        self.assertEqual("abcd", remove_duplicates("abcbd"))
        self.assertEqual("abc", remove_duplicates("aaaabbbaaabbbbcccccaaa"))

    def test_replace_runs_of_space(self):
        self.assertEqual("a b", replace_runs_of_space("a b"))
        self.assertEqual("a b", replace_runs_of_space("a     b"))
        self.assertEqual("the quick brown fox jumps over the lazy dog.", replace_runs_of_space("the        quick   brown   fox               jumps over    the lazy dog.    "))

if __name__ == "__main__":
    unittest.main()
