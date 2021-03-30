#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Implement RandomizedMotifSearch
Rosalind ID: BA2F
URL: http://rosalind.info/problems/ba2f/
"""

import re


def rosalindprint(res, newline=False):
    text = ""
    sep = " "
    if newline:
        sep = "\n"
    for i in res:
        text = text + str(i) + sep
    return text.strip()


def patternprob(pattern, profile):
    """return the probability of observing the pattern with the profile matrix"""
    p = 1
    for x in enumerate(pattern):
        p = p * profile[x[1]][x[0]]
    return p


def kmersindices(text, k):
    """Find indices of all k-mers in text"""
    D = dict()
    for i in range(0, len(text) - k + 1):
        tmp = kmer(text, i, k)
        try:
            D[tmp].append(i)
        except KeyError:
            D[tmp] = [i]
    return D


def kmersfrequency(text, k):
    """Find the number of occurrences of all k-mers in text"""
    D = kmersindices(text, k)
    for k, v in D.items():
        D[k] = len(v)
    return D


def patternprob(pattern, profile):
    """return the probability of observing the pattern with the profile matrix"""
    p = 1
    for x in enumerate(pattern):
        p = p * profile[x[1]][x[0]]
    return p


def ProfileMostProbable(text, k, profile, first=False):
    """
    Find a Profile-most probable k-mer in a string text.
    Profile matrix is represented as a dict.
    """
    maxkey = ""
    maxp = -1
    if first:
        for end in range(k, len(text) + 1):
            key = text[end - k : end]
            tmp = patternprob(key, profile)
            if tmp > maxp:
                maxkey = key
                maxp = tmp
    else:
        D = kmersfrequency(text, k)
        for key in D.keys():
            tmp = patternprob(key, profile)
            if tmp > maxp:
                maxkey = key
                maxp = tmp
    return maxkey


def Motifs(dnalist, profile):
    t = len(dnalist)
    k = len(profile["A"])

    motifs = []
    for i in range(0, t):
        motifs.append(ProfileMostProbable(dnalist[i], k, profile, first=True))
    return motifs


def createprofilematrix(patternlist, pseudocounts=False):
    """
    Returs a profile matrix as a dict based on a the list patternlist
    """
    k = len(patternlist[0])
    D = dict()
    D["A"] = [0] * k
    D["C"] = [0] * k
    D["G"] = [0] * k
    D["T"] = [0] * k

    for pattern in patternlist:
        for x in enumerate(pattern):
            D[x[1]][x[0]] = D[x[1]][x[0]] + 1

    if pseudocounts:
        D["A"] = [x + 1 for x in D["A"]]
        D["C"] = [x + 1 for x in D["C"]]
        D["G"] = [x + 1 for x in D["G"]]
        D["T"] = [x + 1 for x in D["T"]]

    for i in range(0, k):
        s = D["A"][i] + D["C"][i] + D["G"][i] + D["T"][i]
        D["A"][i] = D["A"][i] / s
        D["C"][i] = D["C"][i] / s
        D["G"][i] = D["G"][i] / s
        D["T"][i] = D["T"][i] / s
    return D


def Score(motifs):
    """
    score discrepancy in motifs
    """
    t = len(motifs)

    tmp = "'" + motifs[0] + "'"
    for m in motifs[1:]:
        tmp = tmp + ", '" + m + "'"
    zzip = eval("zip(" + tmp + ")")

    maxcount = []
    for x in zzip:
        As = sum([y == "A" for y in x])
        Cs = sum([y == "C" for y in x])
        Gs = sum([y == "G" for y in x])
        Ts = sum([y == "T" for y in x])
        maxcount.append(t - max(As, Cs, Gs, Ts))
    return sum(maxcount)


def RandomizedMotifSearchAtom(dnalist, k):
    import random

    n = len(dnalist[0])

    randpos = [random.randint(0, n - k) for i in range(0, len(dnalist))]
    bestmotifs = [x[1][x[0] : (x[0] + k)] for x in zip(randpos, dnalist)]
    motifs = bestmotifs

    while True:
        profile = createprofilematrix(motifs, pseudocounts=True)
        motifs = Motifs(dnalist, profile)
        if Score(motifs) < Score(bestmotifs):
            bestmotifs = motifs
        else:
            return bestmotifs


def RandomizedMotifSearch(dnalist, k, N=1000):
    bestmotifs = RandomizedMotifSearchAtom(dnalist, k)
    for i in range(1, N):
        motifs = RandomizedMotifSearchAtom(dnalist, k)
        if Score(motifs) < Score(bestmotifs):
            bestmotifs = motifs
    return bestmotifs


if __name__ == "__main__":

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    k, t = [int(x) for x in inlines[0].strip().split(" ")]
    dnalist = inlines[1:]

    res = RandomizedMotifSearch(dnalist, k, 1000)

    sys.stdout.write(re.sub(" ", "\n", rosalindprint(res)))
