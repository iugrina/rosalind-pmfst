#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Generate the k-mer Composition of a String
Rosalind ID: BA3A
URL: http://rosalind.info/problems/ba3a/
"""


def rosalind_print(result, newline=False):
    text = ""
    sep = " "
    if newline:
        sep = "\n"
    for i in result:
        text = text + str(i) + sep
    return text.strip()


def get_kmer(text, i, k):
    """substring of text from i-th position for the next k letters"""
    return text[i : (i + k)]


def get_kmers(text, k):
    """Find indices of all k-mers in text"""
    kmers = set()
    for i in range(0, len(text) - k + 1):
        kmers.add(get_kmer(text, i, k))
    return kmers


def get_kmer_composition(text, k):
    """Return all kmers appearing in text sorted in lexografical order"""
    return sorted(get_kmers(text, k))


if __name__ == "__main__":

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    k = int(inlines[0])
    text = inlines[1]

    res = get_kmer_composition(text, k)

    sys.stdout.write(rosalind_print(res, newline=True))
