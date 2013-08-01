#! /usr/bin/env python3

import sys
sys.path.append("../dry/lib")
import graphs

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
        neighbor_count = graph.get_neighbors(node)

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
        neighbor_count = graph.get_neighbors(node)

        if (neighbor_count % 2) == 1:
            odd_count += 1

        if odd_count > 2:
            return False

    return odd_count == 2
