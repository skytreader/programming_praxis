#! /usr/bin/env python3

def maximum_subarray(seq):
    first_index = 0
    last_index = 0
    max_val = float("-inf")

    for i in range(len(seq)):
        if i == (last_index - 1):
            temp = max_val
            max_val = max(max_val, max_val + seq[i])
            if temp == max_val:
                # the subsequence chain is broken and we should restart
                max_val = seq[i]
                first_index = i
                last_index = i
     
    return (first_index, last_index)
