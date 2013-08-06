#! /usr/bin/env python3

import sys
import unittest
sys.path.append("../dry/lib")
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

        if (neighbor_count % 2):
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

        if (neighbor_count % 2):
            odd_count += 1

        if odd_count > 2:
            return False

    return odd_count == 2

def eulerian_path(graph):
    """
    Find an Eulerian path in the graph, if one exists. Returns
    the sequence of edges that makes the path. Returns None
    if an Eulerian path is not possible.
    """
    if is_eulerian_path(graph):
        removed_edges = []
        # Find a node with an odd number of neighbors
        cur_node = None

        for node in graph.added_nodes:
            if graph.get_outdegree(node) % 2:
                cur_node = node
                break
        
        node_stack = [cur_node]
        cur_neighbors = graph.get_neighbors(cur_node)

        while node_stack and cur_neighbors:
            if cur_neighbors:
                # Pick a neighbor which will make an edge that
                # is not yet removed.
                chosen_neighbor = None
                for neighbor in cur_neighbors:
                    edge = set([cur_node, neighbor])
                    if edge not in removed_edges:
                        chosen_neighbor = neighbor
                        break

                if chosen_neighbor is None:
                    break

                node_stack.append(cur_node)
                removed_edges.append(set([cur_node, chosen_neighbor]))
                cur_node = chosen_neighbor
                cur_neighbors = graph.get_neighbors(cur_node)
            else:
                # Backtrack here...
                cur_node = node_stack.pop()

        return removed_edges
    else:
        return None

class EulerianTests(unittest.TestCase):
    
    def setUp(self):
        self.eulerian4_circuit = UndirectedAdjList()
        self.eulerian4_circuit.add_nodes(["n1", "n2", "n3", "n4"])
        self.eulerian4_circuit.make_neighbor("n1", "n2")
        self.eulerian4_circuit.make_neighbor("n1", "n3")
        self.eulerian4_circuit.make_neighbor("n2", "n4")
        self.eulerian4_circuit.make_neighbor("n3", "n4")
        
        self.eulerian4_path = UndirectedAdjList()
        self.eulerian4_path.add_nodes(["n1", "n2", "n3", "n4"])
        self.eulerian4_path.make_neighbor("n1", "n2")
        self.eulerian4_path.make_neighbor("n1", "n3")
        self.eulerian4_path.make_neighbor("n2", "n4")
        self.eulerian4_path.make_neighbor("n4", "n3")
        self.eulerian4_path.make_neighbor("n3", "n2")

        self.star_circuit = UndirectedAdjList()
        self.star_circuit.add_nodes(["n1", "n2", "n3", "n4", "n5"])
        self.star_circuit.make_neighbor("n1", "n2")
        self.star_circuit.make_neighbor("n1", "n4")
        self.star_circuit.make_neighbor("n3", "n5")
        self.star_circuit.make_neighbor("n3", "n2")
        self.star_circuit.make_neighbor("n4", "n5")
        self.star_circuit.make_neighbor("n4", "n1")

    def test_eulerian_circuit(self):
        self.assertTrue(is_eulerian_circuit(self.eulerian4_circuit))
        self.assertFalse(is_eulerian_circuit(self.eulerian4_path))
        self.assertTrue(is_eulerian_circuit(self.star_circuit))

    def test_eulerian_path(self):
        self.assertTrue(is_eulerian_path(self.eulerian4_path))
        self.assertFalse(is_eulerian_path(self.star_circuit))
        self.assertFalse(is_eulerian_path(self.eulerian4_circuit))

        # Test determining actual Eulerian path
        eulerianpath = [
            set(["n2", "n1"]),
            set(["n1", "n3"]),
            set(["n3", "n4"]),
            set(["n4", "n2"]),
            set(["n2", "n3"]),
        ]

        self.assertEqual(eulerianpath, eulerian_path(self.eulerian4_path))
        self.assertEqual(None, eulerian_path(self.eulerian4_circuit))
        self.assertEqual(None, eulerian_path(self.star_circuit))

        # Destroy the Eulerian path in eulerian4_path
        self.eulerian4_path.make_neighbor("n1", "n4")
        self.assertFalse(is_eulerian_path(self.eulerian4_path))

if __name__ == "__main__":
    unittest.main()
