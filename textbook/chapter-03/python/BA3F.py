#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Find an Eulerian Cycle in a Graph
Rosalind ID: BA3F
URL: http://rosalind.info/problems/ba3f/
"""


def rosalindInputToGraph(edges):
    D = {}
    for edge in edges:
        first, second = edge.split(" -> ")
        second = second.split(",")
        D[first] = second
    return D


def rosalindOutputToGraph(ecycle):
    D = {}
    nodes = ecycle.split("->")
    for i in range(0, len(nodes) - 1):
        first = nodes[i]
        second = nodes[i + 1]
        if first in D:
            D[first].append(second)
        else:
            D[first] = [second]
    for first in D:
        D[first] = sorted(D[first])
    return D


# will change graph since it is a dict!
def getACycle(graph, possible_starts):
    origin = None
    for start in possible_starts:
        if start in graph:
            origin = start
            break
    if origin is None:
        raise
    cycle = []
    first = origin
    while True:
        if first in graph:
            cycle.append([first, graph[first][0]])
            second = graph[first][0]
            if len(graph[first]) == 1:
                graph.pop(first, None)
            else:
                graph[first] = graph[first][1:]
            if second == origin:
                break
            else:
                first = second
        else:
            break
    return cycle


def start_index(cycle, start):
    s_index = -1
    for i in range(0, len(cycle)):
        if cycle[i][0] == start:
            s_index = i
            break
    return s_index


def eulerianCycle(graph):
    graph = graph.copy()

    cycles = []
    # get all cycles
    possible_starts = list(graph.keys())[:1]
    # possible_starts = ['1140']
    while len(graph) > 0:
        new_cycle = getACycle(graph, possible_starts)
        possible_starts.extend([x[0] for x in new_cycle])
        possible_starts = list(set(possible_starts))
        cycles.append(new_cycle)

    if len(cycles) == 1:
        path = cycles[0]
    else:
        path = cycles[0]
        for i in range(1, len(cycles)):
            next_ = cycles[i]
            s_index = start_index(path, next_[0][0])
            path = path[:s_index] + next_ + path[s_index:]

    firsts = [x[0] for x in path]
    res = "->".join(firsts) + f"->{path[-1][1]}"

    return res


if __name__ == "__main__":

    import sys

    inlines = [x.strip() for x in sys.stdin.readlines()]

    graph = rosalindInputToGraph(inlines)
    res = eulerianCycle(graph)

    sys.stdout.write(res)


#######################
#######################

# filename = "./BA3F.out"
# with open(filename) as f:
#     rout = f.readlines()
#     rout = [x.strip() for x in rout]
#     rout = rout[0]

# routg = rosalindOutputToGraph(rout)


# filename = "./BA3F.input"
# with open(filename) as f:
#     rin = f.readlines()
#     rin = [x.strip() for x in rin]

# ring = rosalindInputToGraph(rin)
