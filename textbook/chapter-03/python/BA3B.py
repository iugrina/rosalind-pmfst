#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Reconstruct a String from its Genome Path
Rosalind ID: BA3B
URL: http://rosalind.info/problems/ba3b/
"""


def rosalindprint(res, newline=False):
    text = ""
    sep = " "
    if newline:
        sep = "\n"
    for i in res:
        text = text + str(i) + sep
    return text.strip()


def string_spelled(patterns):
    """Find the string spelled by a genome path"""
    return patterns[0] + "".join([pattern[-1] for pattern in patterns[1:]])


if __name__ == "__main__":

    import sys

    patterns = [x.strip() for x in sys.stdin.readlines()]

    res = string_spelled(patterns)

    sys.stdout.write(res)
