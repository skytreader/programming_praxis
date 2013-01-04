#! usr/bin/env python

import unittest

"""
http://programmingpraxis.com/2009/05/26/word-search-solver/
UNFINISHED
"""

# TAG
# TODO Check if we can intergrate this pattern for PyGame Objects
UP_LEFT = (-1, -1)
UP = (-1, 0)
UP_RIGHT = (-1, 1)
LEFT = (0, -1)
RIGHT = (0, 1)
DOWN_LEFT = (1, -1)
DOWN = (1, 0)
DOWN_RIGHT = (1, 1)

ALL_DIRECTIONS = [UP_LEFT, UP, UP_RIGHT, LEFT, RIGHT, DOWN_LEFT, DOWN, DOWN_RIGHT]

def search_startswith(prefix, word_set):
    """
    Returns a list of all the words in word_set that starts
    with the given prefix.
    """
    all_starts = []
    
    for word in word_set:
        if word.startswith(prefix):
            all_starts.append(word)
    
    return all_starts

def step_in_directions(row, col, rowlimit, collimit, directions):
    steps = []
    for step_dir in directions:
        drow = row + step_dir[0]
        dcol = col + step_dir[1]

        if (0 <= drow and drow < rowlimit) and (0 <= dcol and dcol < collimit):
            steps.append((drow, dcol, step_dir))

    return steps

def get_neighbors(row, col, rowlimit, collimit, direction):
    """
    The return of this function varies from whether direction is set or
    not. If direction is set, we return the neighbor adjacent to
    (row, col) _in the specified direction_. If there are no more cells
    accessible in that direction, None is returned.

    If direction is not set, we simply return all adjacent neighbors to
    the specified cell.
    """
    if direction:
        return step_in_directions(row, col, rowlimit, collimit, direction)
    else:
        return step_in_directions(row, col, rowlimit, collimit, ALL_DIRECTIONS)

def get_word(cell_seq, letter_block):
    word = ""

    for indices in cell_seq:
        word += letter_block[indices[0]][indices[1]]

    return word

def search(word_set, letter_block):
    """
    Depth-First-Searches for all the words in word_set in letter_block. Returns
    a list of strings specifying the results of the search.
    
    word_set and letter_block is a list of strings. We assume that all the strings
    in letter_block have the same length.
    
    Test cases:
     - w_n in word_set is a prefix of w_m in word_set.
     - intersecting starts: the initial letter of one word in word_set is found in
       the same cell as the initial letter of another word in word_set.

    Let's try two approaches:
      (1) Tag the neighbors of a prefix match cell on what direction are
          they headed (up left, up, up right, ...,etc.).
      (2) Use a tree instead of a stack in storing adjacent cells. The 
          parent-child nodes of the tree will have a "comes from"
          relationship. The tree must allow us access to a node's parent.
          This way, we can derive from what direction do we proceed
          (same as the direction a node's parent took).

    Returns a dictionary of all the words in word_set found and a pair of tuples
    indicating the start indices of the word in the grid and the end indices
    (direction can then be inferred).
    """
    block_height = len(letter_block)
    block_width = len(letter_block[0])
    found_words = dict()
    
    for row in range(block_height):
        for col in range(block_width):
            # print("Origin at " + str(row) + " " + str(col))
            neighbors = get_neighbors(row, col, block_height, block_width, ALL_DIRECTIONS)
            original_prefix = letter_block[row][col]
            match_prefix = letter_block[row][col]
            
            # DFS on all neighbors
            while neighbors:
                current_cell = neighbors.pop()
                # print("Here are the neighbors " + str(neighbors))
                # print("Checking cell " + str(current_cell))
                # PROBLEM
                match_prefix += letter_block[current_cell[0]][current_cell[1]]
                # print("Current prefix " + match_prefix)
                prefix_matches = search_startswith(match_prefix, word_set)
                # print("Prefix matches " + str(prefix_matches))
                
                if prefix_matches:
                    # TEST CASE: neighbors does not get extended (dead-end, possibly).
                    # By next iteration, we must be considering the next neighbor of our origin cell.
                    # print("Extend in same direction: " + str(current_cell[2]))
                    neighbors.extend(get_neighbors(current_cell[0], current_cell[1], block_height, block_width, [current_cell[2]]))
                else:
                    # Return this to original prefix since at next turn, we must be considering the next
                    # neighbor of our origin cell.
                    match_prefix = original_prefix

                if match_prefix in word_set:
                    found_words[match_prefix] = ((row, col), current_cell[0:2])

    # print(str(found_words))
    return found_words

class FunctionTest(unittest.TestCase):
    
    def test_search(self):
        word_list = ["connect", "praxis", "genius", "compute", "free", "mining"]
        word_grid = ["gacbcpcdef", "geohorijkl", "mnnomapqrs", "tunipxvwxy", "freeuizgab", "cdcetsnfgh", "ijtkeilmno", "pqrsntuvwx", "yzaibcdefg", "himjklmnop"]
        self.assertEqual(len(word_grid), 10)
        
        for row in word_grid:
            # print("Checking row " + str(row))
            self.assertEqual(len(row), 10)

        expected_output = dict()
        expected_output["connect"] = ((0, 2), (6, 2))
        expected_output["praxis"] = ((0, 5), (5, 5))
        expected_output["genius"] = ((0, 0), (5, 5))
        expected_output["compute"] = ((0, 4), (6, 4))
        expected_output["free"] = ((4, 0), (4, 3))
        expected_output["mining"] = ((9, 2), (4, 7))

        self.assertEqual(expected_output, search(word_list, word_grid))

if __name__ == "__main__":
    unittest.main()
