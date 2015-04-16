import unittest

def match_count(haystack, needle):
    """
    Return all instances of needle in haystack, whether as a substring or as a
    subsequence.
    """
    return 0

class FunctionsTest(unittest.TestCase):
    
    def test_fun(self):
        self.assertEqual(3, match_count("catapult", "cat"))
        self.assertEqual(7, match_count("bxaxxtxxbxbxxaxxtxtxa", "bat"))

if __name__ == "__main__":
    unittest.main()
