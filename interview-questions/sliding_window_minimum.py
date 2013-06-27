#! /usr/bin/env python3

"""
http://programmingpraxis.com/2011/02/22/sliding-window-minimum/
UNFINISHED
"""

def harter_sliding(numlist, window):
    first_window_min = min(numlist[0:window])
    ascending_minq = [first_window_min]

