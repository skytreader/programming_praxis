import unittest

"""
http://programmingpraxis.com/2015/03/10/count-all-matches/

unifinshed
"""

def simplify(haystack, needle):
    """
    Simplify is two steps:
    
    (1) Remove all characters of haystack not in needle.
    (2) From what remains of (1), the starting and ending letter must be equal to the
        starting and ending letter of needle.
    """
    simplified = []
    
    for hay in haystack:
        if hay in needle:
            simplified.append(hay)
    
    for hay in simplified:
        if hay == needle[0]:
            break
        else:
            simplified.pop(0)

    for rev_index in reversed(range(len(simplified))):
        if simplified[rev_index] == needle[-1]:
            break
        else:
            simplified.pop()

    return "".join(simplified)

def match_count(haystack, needle):
    """
    Return all instances of needle in haystack, whether as a substring or as a
    subsequence.
    """
    simple_hay = simplify(haystack)
    curword = ""
    needle_index = 0
    count = 0

    for hay in haystack:
        if hay == needle[needle_index]:
            needle_index += 1

    return count

class FunctionsTest(unittest.TestCase):
    
    def test_fun(self):
        self.assertEqual(3, match_count("catapult", "cat"))
        self.assertEqual(7, match_count("bxaxxtxxbxbxxaxxtxtxa", "bat"))
        self.assertEqual(27, match_count("tttaaappp", "tap"))

if __name__ == "__main__":
    unittest.main()
