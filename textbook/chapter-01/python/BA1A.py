#!/usr/bin/env python3

"""
A solution to a ROSALIND bioinformatics problem.

Problem Title: Compute the Number of Times a Pattern Appears in a Text
Rosalind ID: BA1A
URL: http://rosalind.info/problems/ba1a/
"""


def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i:(i+k)]


def patterncount(text, pattern):
    """Find a number of time pattern is within a text"""
    count = 0
    np = len(pattern)
    for i in range(0, len(text) - np + 1):
        if kmer(text, i, np) == pattern:
            count = count + 1
    return count


if __name__ == '__main__':

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    text = inlines[0]
    pattern = inlines[1]

    res = patterncount(text, pattern)

    sys.stdout.write(str(res))
