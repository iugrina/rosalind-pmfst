#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Implement MotifEnumeration
Rosalind ID: BA2A
URL: http://rosalind.info/problems/ba2a/
"""


def rosalindprint(res, newline=False):
    text = ""
    sep = " "
    if newline:
        sep = "\n"
    for i in res:
        text = text + str(i) + sep
    return text.strip()


def kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i : (i + k)]


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


def HammingDistance(p, q):
    """Computes the hamming distance between strings p and q"""
    if len(p) != len(q):
        return -1

    dist = 0
    for first, second in zip(p, q):
        if first != second:
            dist = dist + 1

    return dist


def ApproximatePatternMatching(text, pattern, d):
    """Find All Approximate Occurrences of a Pattern in a String"""
    D = kmersindices(text, len(pattern))
    L = list()
    [L.extend(value) for key, value in D.items() if HammingDistance(key, pattern) <= d]
    return sorted(L)


def ApproximatePatternCount(text, pattern, d):
    """total number of occurrences of Pattern in Text with at most d mismatches"""
    L = ApproximatePatternMatching(text, pattern, d)
    return len(L)


def subsets(n, k):
    """return all k-sized subsets (as indices) of an n-sized set"""

    if k == 0:
        return [[0] * n]

    def helper(l, lastn):
        if sum(l) < lastn or lastn < 1:
            return []
        for i in range(len(l) - 1, -1, -1):
            if l[i] == 1:
                lastind = i
                break
        head = l[: (lastind - lastn + 1)]
        N = len(l) - len(head)
        res = [
            head + [0] * i + [1] * lastn + [0] * (N - i - lastn)
            for i in range(0, N - lastn + 1)
        ]
        return res

    def recursion(l, lastn):
        tmp = helper(l, lastn)
        if lastn == 1:
            return tmp
        L = []
        for x in tmp:
            L.extend(recursion(x, lastn - 1))
        return L

    startlist = [1] * k + [0] * (n - k)
    return recursion(startlist, k)


def mutations(pattern, errorind):
    """Generate all mutatios for a pattern at indices given in errorind
    such that Hamming distance is equal to the sum(errorind)"""

    def f(base, start=""):
        if base == "A":
            return [start + "C", start + "G", start + "T"]
        if base == "C":
            return [start + "A", start + "G", start + "T"]
        if base == "G":
            return [start + "A", start + "C", start + "T"]
        if base == "T":
            return [start + "A", start + "C", start + "G"]

    L = [""]

    for base, error in zip(pattern, errorind):
        if error == 0:
            L = [x + base for x in L]
        else:
            tmp = [f(base, x) for x in L]
            L = []
            [[L.append(x) for x in xl] for xl in tmp]
    return L


def WordsWithMismatch(text, k, d):
    """Find all k-mers (words) with up to d mismatches in a string text"""
    D = kmersfrequency(text, k)

    errors = []
    for d in range(0, d + 1):
        errors.extend(subsets(k, d))

    L = []
    for x in D.keys():
        for errorind in errors:
            L.extend(mutations(x, errorind))
    L = list(set(L))

    RES = dict()
    for pattern in L:
        RES[pattern] = ApproximatePatternCount(text, pattern, d)
    return RES


def MotifEnumeration(dnalist, k, d):
    L = list()
    for dna in dnalist:
        L.append(WordsWithMismatch(dna, k, d))
    RES = dict()
    for D in L:
        for k in D.keys():
            try:
                RES[k] = RES[k] + 1
            except KeyError:
                RES[k] = 1
    return [k for k, v in RES.items() if v == len(dnalist)]


if __name__ == "__main__":

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    k, d = [int(x) for x in inlines[0].split(" ")]
    L = list()
    for i in range(1, len(inlines)):
        L.append(inlines[i])

    res = MotifEnumeration(L, k, d)

    sys.stdout.write(rosalindprint(res))
