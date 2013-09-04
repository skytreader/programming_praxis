#! /usr/bin/env python3

import string
import unittest

"""
http://programmingpraxis.com/2009/12/15/affine-shift-cipher/
UNFINISHED

All indices are zero-based.
"""

def to_letters(numlist):
    """
    Returns in uppercase.
    """
    return "".join([string.ascii_uppercase[i] for i in numlist])

def to_numbers(letters):
    return [string.ascii_uppercase.index(x) for x in letters]

def affine(message, a, b, fun):
    numlist = to_numbers(message)
    affined = []

    for num in numlist:
        affined.append(fun(a, b, num))

    return to_letters(affined)

def encrypt(a, b, x):
    return ((a * x) + b) % 26

def affine_encrypt(message, a, b):
    return affine(message, a, b, encrypt)

def decrypt(a, b, x):
    pass

def affine_decrypt(message, a, b):
    return affine(message, a, b, decrypt)

class FunctionsTest(unittest.TestCase):
    
    def test_to_letters(self):
        self.assertEqual("ABC", to_letters([0, 1, 2]))

    def test_affine_encrypt(self):
        test_string = "PROGRAMMINGPRAXIS"
        encrypted = affine_encrypt(test_string, 5, 8)
        expected = "FPAMPIQQWVMFPITWU"
        self.assertEqual(encrypted, expected)

    def test_affine_decrypt(self):
        test_string = "FPAMPIQQWVMFPITWU"
        expected = "PROGRAMMINGPRAXIS"
        decrypted = affine_decrypt(test_string, 5, 8)
        self.assertEqual(decrypted, expected)

if __name__ == "__main__":
    unittest.main()
