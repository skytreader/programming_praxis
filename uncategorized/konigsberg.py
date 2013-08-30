#! /usr/bin/env python3

import random
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

def nodes_to_edges(nodes):
    """
    Takes in a list of nodes (assuming they form a path) and returns a list of
    edges describing the same path. A list of edges is represented as a list
    of sets.
    """
    edge_path = []
    limit = len(nodes) - 1
    i = 0

    while i < limit:
        edge_path.append(set([nodes[i], nodes[i + 1]]))
        i += 1

    return edge_path

def path_start_node(graph):
    """
    Start node function for finding Eulerian paths. Assumes that an Eulerian
    path is possible in the graph.
    """
    for node in graph.added_nodes:
        if graph.get_outdegree(node) % 2:
            return node

def circuit_start_node(graph):
    """
    Start node function for finding Eulerian circuits. Assumes that an Eulerian
    circuit is possible in the graph.
    """
    return random.choice(list(graph.added_nodes))

def eulerian(start_fun, verification, graph):
    """
    Abstraction function for getting an Eulerian path/circuit in the graph. The
    difference will be in how the initial node is chosen.

    start_fun is a function that takes in a graph and returns an appropriate
    initial node.

    verification is a function that checks whether a graph has an Eulerian
    path/circuit. Note that it must coincide with the start_fun.
    """
    if verification(graph):
        path = []
        cur_node = start_fun(graph)
        print("LOG Initial node chosen: " + str(cur_node))
        node_stack = [cur_node]
        cur_neighbors = graph.get_neighbors(cur_node)

        while node_stack and cur_neighbors:
            if cur_neighbors:
                # Pick a neighbor which will make an edge that
                # is not yet removed.
                chosen_neighbor = None
                for neighbor in cur_neighbors:
                    edge = set([cur_node, neighbor])
                    if edge not in path:
                        chosen_neighbor = neighbor
                        break

                print("LOG Chose a neighbor: " + str(chosen_neighbor))

                if chosen_neighbor is None:
                    break

                node_stack.append(cur_node)
                path.append(cur_node)
                cur_node = chosen_neighbor
                print("LOG Current node is now: " + cur_node)
                cur_neighbors = graph.get_neighbors(cur_node)
            else:
                # Backtrack here...
                cur_node = node_stack.pop()
                print("LOG Backtracking! Current node is now: " + str(cur_node))

        return path
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

        self.line = UndirectedAdjList()
        self.line.add_nodes(["n1", "n2", "n3", "n4"])
        self.line.make_neighbor("n1", "n2")
        self.line.make_neighbor("n2", "n3")
        self.line.make_neighbor("n3", "n4")

    def test_eulerian_circuit(self):
        self.assertTrue(is_eulerian_circuit(self.eulerian4_circuit))
        self.assertFalse(is_eulerian_circuit(self.eulerian4_path))
        self.assertTrue(is_eulerian_circuit(self.star_circuit))
        self.assertFalse(is_eulerian_circuit(self.line))
        
        # TODO Characterize Eulerian circuits for unit test checking
        present_nodes = set(["n1", "n2", "n3", "n4"])
        
        circuit = eulerian(circuit_start_node, is_eulerian_circuit, self.eulerian4_circuit)
        print(str(circuit))
        foo = present_nodes == set(circuit)
        self.assertTrue(foo)

        self.assertEqual(None, eulerian(circuit_start_node,
            is_eulerian_circuit, self.eulerian4_circuit))

    def test_eulerian_path(self):
        self.assertTrue(is_eulerian_path(self.eulerian4_path))
        self.assertFalse(is_eulerian_path(self.star_circuit))
        self.assertFalse(is_eulerian_path(self.eulerian4_circuit))
        self.assertTrue(is_eulerian_path(self.line))

        # Test determining actual Eulerian path
        # TODO Better characterization of Eulerian paths.
        eulerianpath = [
            set(["n2", "n1"]),
            set(["n1", "n3"]),
            set(["n3", "n4"]),
            set(["n4", "n2"]),
            set(["n2", "n3"]),
        ]

        self.assertEqual(eulerianpath, eulerian(path_start_node,
            is_eulerian_path, self.eulerian4_path))
        self.assertEqual(None, eulerian(path_start_node,
            is_eulerian_path, self.eulerian4_circuit))
        self.assertEqual(None, eulerian(path_start_node,
            is_eulerian_path, self.star_circuit))

        # Destroy the Eulerian path in eulerian4_path
        self.eulerian4_path.make_neighbor("n1", "n4")
        self.assertFalse(is_eulerian_path(self.eulerian4_path))

if __name__ == "__main__":
    unittest.main()
