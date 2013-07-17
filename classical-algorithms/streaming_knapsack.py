#! /usr/bin/env python3

"""
http://programmingpraxis.com/2012/05/15/streaming-knapsack/
"""

class Stream(object):
    
    def __init__(self, target):
        self.target = target
        self.stream = []
        self.bins = []
        self.subseq_found = []
    
    def add_to_stream(self, addition):
        self.stream.append(addition)
        is_added = False
        for numbin in self.bins:
            total = sum(numbin)

            if (total + addition) == self.target:
                numbin.append(addition)
                self.subseq_found = numbin
                is_added = True
                break

            if (total + addition) < self.target:
                self.bins.append(numbin)
                numbin.append(addition)
                is_added = True

        if not is_added:
            self.bins.append([addition])

if __name__ == "__main__":
    test = Stream(20)
    stream = [4, 8, 9, 2, 10, 2,17,2,12,4, 5]

    for number in stream:
        test.add_to_stream(number)
        print(test.stream)
        print(test.bins)

        if test.subseq_found:
            print("In " + str(test.stream) + " found " + str(test.subseq_found))
