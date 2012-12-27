#! /usr/bin/env python3

import unittest

"""
http://programmingpraxis.com/2012/03/02/balanced-delimiters/
"""

OPENERS = "([{<"
CLOSERS = ")]}>"

def is_balanced(s):
    opener_stack = []
    last_quote = None
    delimiter_mode = True
    last_character = None

    for c in s:
        if delimiter_mode and last_character != "\\":
            if c in OPENERS:
                opener_stack.append(c)
            elif c in CLOSERS:
                try:
                    matching_opener = opener_stack.pop()
                    if OPENERS.index(matching_opener) != CLOSERS.index(c):
                        return False
                except IndexError:
                    return False
            elif c == '"' or c == "'":
                delimiter_mode = False
                last_quote = c
        elif c == '"' or c == "'":
            delimiter_mode = c == last_quote

        last_character = c
    
    return not len(opener_stack)

class FunctionsTest(unittest.TestCase):
    
    def test_is_balanced(self):
        self.assertTrue(is_balanced("([{<>}])"))
        self.assertFalse(is_balanced("(()"))
        self.assertFalse(is_balanced("[())"))
        self.assertTrue(is_balanced("\"'''\"()"))
        self.assertTrue(is_balanced("'\"\"\"'()"))
        self.assertTrue(is_balanced("'[())'"))
        self.assertTrue(is_balanced(""))
        self.assertTrue(is_balanced("'\\'()'()"))

if __name__ == "__main__":
    unittest.main()
