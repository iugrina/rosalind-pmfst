#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Implement NumberToPattern
URL: http://rosalind.info/problems/ba1M/
"""


def NumberToPattern(index, k):
    pattern = list()
    D = {0: 'A', 1: 'C', 2: 'G', 3: 'T'}
    q = index
    for i in range(0, k):
        r = q % 4
        q = q // 4
        pattern.append(D[r])
    return("".join(pattern[::-1]))


if __name__ == '__main__':

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    index = int(inlines[0])
    k = int(inlines[1])

    res = NumberToPattern(index, k)

    sys.stdout.write(str(res))
