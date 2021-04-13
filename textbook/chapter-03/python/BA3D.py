#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Construct the De Bruijn Graph of a String
Rosalind ID: BA3D
URL: http://rosalind.info/problems/ba3d/
"""


def rosalindprint(D):
    out = ""
    keys = sorted(D.keys())
    for first in keys:
        second = ",".join(sorted(D[first]))
        out = out + f"{first} -> {second}\n"
    return out


def deBrujinGraph(k, text):
    D = {}
    for i in range(0, len(text) - k + 1):
        first = text[i : (i + k - 1)]
        second = text[(i + 1) : (i + k)]
        if first not in D:
            D[first] = [second]
        else:
            D[first].append(second)
    return D


if __name__ == "__main__":

    import sys

    inlines = [x.strip() for x in sys.stdin.readlines()]
    k = int(inlines[0])
    text = inlines[1]

    res = deBrujinGraph(k, text)

    sys.stdout.write(rosalindprint(res))
