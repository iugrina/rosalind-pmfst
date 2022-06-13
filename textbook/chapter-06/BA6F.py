#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Implement ChromosomeToCycle
Rosalind ID: BA6F
URL: http://rosalind.info/problems/ba6f/
"""


def rosalind_input(text):
    tmp = [int(x) for x in text[1:-1].split(" ")]
    return tmp


def chromosome_to_cycle(chromosome):
    cycle = []
    for x in chromosome:
        if x > 0:
            cycle.extend([2 * x - 1, 2 * x])
        if x < 0:
            x = abs(x)
            cycle.extend([2 * x, 2 * x - 1])
    return cycle


def rosalind_print(cycle):
    return "(" + " ".join([str(x) for x in cycle]) + ")"


if __name__ == "__main__":

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    text = inlines[0]

    res = chromosome_to_cycle(rosalind_input(text))

    print(rosalind_print(res))
