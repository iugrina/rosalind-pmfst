#!/usr/bin/env python3

"""
A solution to a ROSALIND bioinformatics problem.

Problem Title: Find the Most Frequent Words in a String
Rosalind ID: BA1B
URL: http://rosalind.info/problems/ba1b/
"""


def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]


def kmersfrequency(text, k):
    D = dict()
    for i in range(0, len(text) - k + 1):
        tmp = kmer(text, i, k)
        try:
            D[tmp] = D[tmp] + 1
        except KeyError:
            D[tmp] = 1
    return(D)


def mostfrequentkmers(text, k):
    D = kmersfrequency(text, k)
    maxcount = max(D.values())
    return dict.fromkeys([x[0] for x in D.items() if x[1] == maxcount],
                         maxcount)


if __name__ == '__main__':

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    text = inlines[0]
    k = int(inlines[1])

    res = mostfrequentkmers(text, k)

    sys.stdout.write(str(res))
