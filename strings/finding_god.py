#! /usr/bin/env python3

from string import ascii_letters
import unittest
import sys
sys.path.append("../pydagogical")
from data_structures.graphs import AdjacencyLists

"""
https://programmingpraxis.com/2016/02/16/finding-god/

Assumption, paths that lead off farther than the last line "die off". If the
last line does not have enough words to sustain a path, it does not go
anywhere else.
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

    Returns a graph with the given nodes linked as per the constraints of the
    problem.
    """
    graph = AdjacencyLists()

    for ri, l in enumerate(num_nodes):
        graph.add_nodes([(ri, ci) for ci, n in enumerate(l)])

    for ri, l in enumerate(num_nodes):
        for ci, n in enumerate(l):
            if (ci + n) < len(l):
                graph.make_neighbors((ri, ci), (ri, ci + n))
            else:
                jumps = ci + n
                _ri, _ci = ri, ci
                
                while jumps != 0 and _ri < len(num_nodes):
                    deductible = jumps - (len(l) - _ci)
                    jumps -= deductible
                    # Because after current row, the column index resets.
                    _ci = 0

                    if jumps < 0:
                        _ci = len(num_nodes[_ri]) + jumps
                        break

                    _ri += 1

                if _ri < len(num_nodes):
                    graph.make_neighbors((ri, ci), (_ri, _ci))
                        

class FunctionsTest(unittest.TestCase):
    
    def test_convert_to_letter_counts(self):
        spam = "In the beginning God created the heaven and the earth."
        spam_lc = [2, 3, 9, 3, 7, 3, 6, 3, 3, 5]
        self.assertEqual(spam_lc, convert_to_letter_counts(spam))

if __name__ == "__main__":
    unittest.main()
