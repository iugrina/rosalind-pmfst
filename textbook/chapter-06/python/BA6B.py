#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Number of Breakpoints Problem
Rosalind ID: BA6B
URL: http://rosalind.info/problems/ba6b/
"""


def rosalind_input(text):
    tmp = [int(x) for x in text[1:-1].split(" ")]
    return [0] + tmp + [len(tmp) + 1]


def is_adjacency(pair):
    if pair[1] - pair[0] == 1:
        return True
    return False


def n_adjacencies(permutation):
    count = 0
    for i in range(len(permutation) - 1):
        count += is_adjacency((permutation[i], permutation[i + 1]))
    return count


def n_breakpoints(permutation):
    # permutation here contains 0 and n+1 also so we need -1
    return len(permutation) - 1 - n_adjacencies(permutation)


if __name__ == "__main__":

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    text = inlines[0]

    res = n_breakpoints(rosalind_input(text))

    print(res)
