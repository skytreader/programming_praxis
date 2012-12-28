#! /usr/bin/env python3

import unittest

"""
Interface and implementations of a tree abstract data type.
"""

class Tree(object):
    """
    Implementations should make it clear whether the arguments passed for
    node is an index or an actual object. If, for an implementation, a
    certain method is not supported, raise a NotImplementedError .
    """
    
    def add_node(self, node_contents):
        pass

    def get_nodes(self, node_contents):
        pass

    def get_children(self, node):
        pass

    def get_parent(self, node):
        """
        Should return None if the node indicated is root. Should return
        a list of all
        """
        pass

class ListTree(Tree):
    """
    Implements a tree as a list-of-lists. Don't use this if you need
    to store multiple shallow copies of data in a single tree.
    """

    def __init__(self):
        self.__nodes = []
    
    def add_node(self, node_contents):
        self.__nodes.append([node_contents])

    def get_nodes(self):
        return list(map(lambda x: x[0], self.__nodes))

    def link_child(self, parent, child):
        """
        Links nodes parent and child. If there are several shallow copies
        of either parent or child scattered in in the tree, only the first
        copy inserted is used.
        
        TODO Test with deep and shallow copies.
        """
        nodelist = self.get_nodes()
        parent_index = nodelist.index(parent)
        child_index = nodelist.index(child)

        self.__nodes[parent_index].append(child)

class ListTreeTests(unittest.TestCase):
    
    def setup(self):
        pass
