#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Implement CycleToChromosome
Rosalind ID: BA6G
URL: http://rosalind.info/problems/ba6g/
"""


def rosalind_input(text):
    tmp = [int(x) for x in text[1:-1].split(" ")]
    return tmp


def cycle_to_chromosome(cycle):
    chromosome = [chromosome]
    for i in range(0, len(cycle), 2):
        if cycle[i] < cycle[i + 1]:
            chromosome.append(cycle[i + 1] // 2)
        if cycle[i] > cycle[i + 1]:
            chromosome.append(-1 * cycle[i] // 2)
    return chromosome


def f(x):
    if x >= 0:
        return f"+{x}"
    else:
        return f"{x}"


def rosalind_print(cycle):
    return "(" + " ".join([f(x) for x in cycle]) + ")"


if __name__ == "__main__":

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    text = inlines[0]

    res = cycle_to_chromosome(rosalind_input(text))

    print(rosalind_print(res))
