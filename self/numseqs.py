#! /usr/bin/env python3

def golomb(n):
    """
    Produce a Golomb Sequence of size n.
    """
    current_number = 1
    repeat_count = 0
    seq = []

    for i in range(n):
        if len(seq) >= current_number:
            num_count = seq[current_number - 1]

            if repeat_count >= num_count:
                current_number += 1
                repeat_count = 0

            seq.append(current_number)
        else:
            seq.append(current_number)

        repeat_count += 1

    return seq

def look_and_say(seed, n):
    """
    Produce a look-and-say sequence with the given seed and of length n.
    """

    def find_contiguous_sequence(s, start_index):
        """
        Returns the length of a sequence of continuous characters from the given
        start_index.
        """
        sc = s[start_index]
        count = 1
        _s = s[start_index+1:]

        for c in _s:
            if c == sc:
                count += 1
            else:
                break
        
        return count
            
    seq = [seed]

    for i in range(n):
        last_string = str(seq[-1])
        next_string = []
        limit = len(last_string)
        desc_index = 0

        while desc_index < limit:
            cs_count = find_contiguous_sequence(last_string, desc_index)
            next_string.append(str(cs_count) + last_string[desc_index])
            desc_index += cs_count

        seq.append("".join(next_string))

    return seq


if __name__ == "__main__":
    print(golomb(100))
    print(look_and_say(1, 8))
