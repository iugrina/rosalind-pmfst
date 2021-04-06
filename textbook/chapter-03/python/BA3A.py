#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Generate the k-mer Composition of a String
Rosalind ID: BA3A
URL: http://rosalind.info/problems/ba3a/
"""


def rosalindprint(res, newline=False):
    text = ""
    sep = " "
    if newline:
        sep = "\n"
    for i in res:
        text = text + str(i) + sep
    return text.strip()


def kmerComposition(text, k):
    """Return all kmers appearing in text sorted in lexografical order"""
    tmp = sorted([text[i : (i + k)] for i in range(0, len(text) - k + 1)])
    return tmp


if __name__ == "__main__":

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    k = int(inlines[0])
    text = inlines[1]

    res = kmerComposition(text, k)

    sys.stdout.write(rosalindprint(res, newline=True))
