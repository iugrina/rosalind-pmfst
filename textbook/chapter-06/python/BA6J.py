#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Implement 2-BreakOnGenomeGraph
Rosalind ID: BA6J
URL: http://rosalind.info/problems/ba6j/
"""


def string_to_int_repr(text):
    return [int(x) for x in text.strip("(, ").split(",")]


def rosalind_input_edges(text):
    edges = text.split(")")[:-1]
    edges = [string_to_int_repr(edge) for edge in edges]
    return edges


def rosalind_input_two_breaks(text):
    tmp = text.split(",")
    two_breaks = [int(x) for x in tmp]
    return two_breaks


def two_break_on_genome_graph(edges, two_breaks):
    helper = edges.copy()
    for edge in edges:
        if edge[0] in two_breaks:
            helper.remove(edge)

    helper.append([two_breaks[0], two_breaks[2]])
    helper.append([two_breaks[1], two_breaks[3]])

    return helper


def rosalind_print(edges):
    tuples = [tuple(x) for x in edges]
    return repr(tuples)[1:-1]


if __name__ == "__main__":

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]

    colored = inlines[0]
    two_breaks = inlines[1]

    colored = rosalind_input_edges(colored)
    two_breaks = rosalind_input_two_breaks(two_breaks)

    ggraph = two_break_on_genome_graph(colored, two_breaks)

    print(rosalind_print(ggraph))
