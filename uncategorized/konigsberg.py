#! /usr/bin/env python3

import sys
import unittest
sys.path.append("../lib")
from graphs import UndirectedAdjList

"""
http://programmingpraxis.com/2013/05/31/the-seven-bridges-of-knigsberg/
UNFINISHED
"""

def is_eulerian_circuit(graph):
    """
    Determines whether an Eulerian circuit exists in the
    given graph.
    """
    # TODO Graph library is not updated
    for node in graph.added_nodes:
        neighbor_count = len(graph.get_neighbors(node))

        if (neighbor_count % 2) == 1:
            return False

    return True

def is_eulerian_path(graph):
    """
    Determines whether an Eulerian path exists in the given
    graph.
    """
    odd_count = 0

    for node in graph.added_nodes:
        neighbor_count = len(graph.get_neighbors(node))

        if (neighbor_count % 2) == 1:
            odd_count += 1

        if odd_count > 2:
            return False

    return odd_count == 2

class EulerianTests(unittest.TestCase):
    
    def setUp(self):
        self.eulerian4_circuit = UndirectedAdjList()
        self.eulerian4_circuit.add_nodes(["n1", "n2", "n3", "n4"])
        self.eulerian4_circuit.make_neighbor("n1", "n2")
        self.eulerian4_circuit.make_neighbor("n1", "n3")
        self.eulerian4_circuit.make_neighbor("n2", "n4")
        self.eulerian4_circuit.make_neighbor("n3", "n4")
        
        self.non_eulerian4 = UndirectedAdjList()
        self.non_eulerian4.add_nodes(["n1", "n2", "n3", "n4"])
        self.non_eulerian4.make_neighbor("n1", "n2")
        self.non_eulerian4.make_neighbor("n1", "n3")
        self.non_eulerian4.make_neighbor("n2", "n4")
        self.non_eulerian4.make_neighbor("n4", "n3")
        self.non_eulerian4.make_neighbor("n3", "n2")

    def test_eulerian_circuit(self):
        self.assertTrue(is_eulerian_circuit(self.eulerian4_circuit))
        self.assertFalse(is_eulerian_circuit(self.non_eulerian4))

if __name__ == "__main__":
    unittest.main()
