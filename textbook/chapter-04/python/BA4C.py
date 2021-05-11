#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Generate the Theoretical Spectrum of a Cyclic Peptide
Rosalind ID: BA4C
URL: http://rosalind.info/problems/ba4c/
"""


def rosalindprint(res):
    return " ".join([str(x) for x in res])


def get_amino_acid_mass():
    mass = {
        "G": 57,
        "A": 71,
        "S": 87,
        "P": 97,
        "V": 99,
        "T": 101,
        "C": 103,
        "I": 113,
        "L": 113,
        "N": 114,
        "D": 115,
        "K": 128,
        "Q": 128,
        "E": 129,
        "M": 131,
        "H": 137,
        "F": 147,
        "R": 156,
        "Y": 163,
        "W": 186,
    }

    return mass


def spectrum(peptide):
    n = len(peptide)
    mass = get_amino_acid_mass()

    extended_peptide = peptide + peptide[:-1]

    spectrum = []
    spectrum.append(0)
    spectrum.append(sum([mass[x] for x in peptide]))

    for l in range(n):
        for k in range(1, n):
            subpeptide = extended_peptide[l : l + k]
            spectrum.append(sum([mass[x] for x in subpeptide]))

    return sorted(spectrum)


if __name__ == "__main__":

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    peptide = inlines[0]

    res = spectrum(peptide)

    sys.stdout.write(rosalindprint(res))
