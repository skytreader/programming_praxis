#! /usr/bin/env python3

import unittest

"""
http://programmingpraxis.com/2011/02/15/google-code-jam-qualification-round-africa-2010/
UNFINISHED
"""

# Store credit

def buy_with_credit(credit, pricelist):
    """This is basically the sum of two integers problem solved previously."""
    matchingindices = []
    price_index = 0
    item_count = len(pricelist)

    for price in pricelist:
        remains = credit - price

        if remains in pricelist[0:price_index] or remains in pricelist[price_index + 1: item_count]:
            remains_index = pricelist.index(remains, price_index + 1)
            return (price_index + 1, remains_index + 1) if min(price_index, remains_index) == price_index else (remains_index + 1, price_index + 1)

        price_index += 1

    return None

# Reverse words

def reverse_words(sentence_list):
    reversed_sentences = []

    for sentence in sentence_list:
        words = sentence.split(" ")
        words.reverse()
        reversed_sentences.append(" ".join(words))

    return reversed_sentences

# T9 spelling
keys = [" ", None, "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

def find_key(letter):
    limit = len(keys)
    for key in range(limit):
        if keys[key] is not None and keys[key].find(letter) >= 0:
            return key

def t9_encode(message):
    t9_encoded = ""
    previous_key = None

    for letter in message:
        key = find_key(letter)

        if key == previous_key:
            t9_encoded += " "

        previous_key = key

        key_presses = keys[key].index(letter) + 1
        t9_encoded += str(key) * key_presses

    return t9_encoded

class FunctionsTest(unittest.TestCase):
    
    def test_buy_with_credit(self):
        test1 = buy_with_credit(100, [5, 75, 25])
        self.assertEqual(test1, (2, 3))
        
        test2 = buy_with_credit(200, [150,24,79,50,88,345,3])
        self.assertEqual(test2, (1, 4))

        test3 = buy_with_credit(8, [2,1,9,4,4,56,90,3])
        self.assertEqual(test3, (4, 5))

    def test_reverse_words(self):
        sentence_list = ["this is a test", "foobar", "all your base"]
        reversed_list = ["test a is this", "foobar", "base your all"]

        self.assertEqual(reverse_words(sentence_list), reversed_list)

    def test_t9_encode(self):
        self.assertEqual(t9_encode("hi"), "44 444")
        self.assertEqual(t9_encode("yes"), "999337777")
        self.assertEqual(t9_encode("foo  bar"), "333666 6660 022 2777")
        self.assertEqual(t9_encode("aa"), "2 2")
        self.assertEqual(t9_encode("b"), "22")
        self.assertEqual(t9_encode("hello world"), "4433555 555666096667775553")

if __name__ == "__main__":
    unittest.main()
