#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Find Substrings of a Genome Encoding a Given Amino Acid String 
Rosalind ID: BA4B
URL: http://rosalind.info/problems/ba4b/
"""


def rosalindprint(res):
    return "\n".join(res)


def get_genetic_code_codons(three_to_one=True):
    genetic_code = {
        "AAA": "K",
        "AAC": "N",
        "AAG": "K",
        "AAU": "N",
        "ACA": "T",
        "ACC": "T",
        "ACG": "T",
        "ACU": "T",
        "AGA": "R",
        "AGC": "S",
        "AGG": "R",
        "AGU": "S",
        "AUA": "I",
        "AUC": "I",
        "AUG": "M",
        "AUU": "I",
        "CAA": "Q",
        "CAC": "H",
        "CAG": "Q",
        "CAU": "H",
        "CCA": "P",
        "CCC": "P",
        "CCG": "P",
        "CCU": "P",
        "CGA": "R",
        "CGC": "R",
        "CGG": "R",
        "CGU": "R",
        "CUA": "L",
        "CUC": "L",
        "CUG": "L",
        "CUU": "L",
        "GAA": "E",
        "GAC": "D",
        "GAG": "E",
        "GAU": "D",
        "GCA": "A",
        "GCC": "A",
        "GCG": "A",
        "GCU": "A",
        "GGA": "G",
        "GGC": "G",
        "GGG": "G",
        "GGU": "G",
        "GUA": "V",
        "GUC": "V",
        "GUG": "V",
        "GUU": "V",
        "UAA": "*",
        "UAC": "Y",
        "UAG": "*",
        "UAU": "Y",
        "UCA": "S",
        "UCC": "S",
        "UCG": "S",
        "UCU": "S",
        "UGA": "*",
        "UGC": "C",
        "UGG": "W",
        "UGU": "C",
        "UUA": "L",
        "UUC": "F",
        "UUG": "L",
        "UUU": "F",
    }

    if three_to_one:
        return genetic_code
    else:
        G = {}
        for k, v in genetic_code.items():
            if v not in G:
                G[v] = [k]
            else:
                G[v].append(k)
        return G


def get_all_combinations_worker(
    peptide, codons_one_to_three, current_status, all_combinations
):
    if len(peptide) == 0:
        all_combinations.append(current_status)
        return

    for codon in codons_one_to_three[peptide[0]]:
        get_all_combinations_worker(
            peptide[1:], codons_one_to_three, current_status + codon, all_combinations
        )


def get_all_combinations(peptide):
    codons_one_to_three = get_genetic_code_codons(three_to_one=False)
    current_status = ""
    all_combinations = []

    get_all_combinations_worker(
        peptide, codons_one_to_three, current_status, all_combinations
    )

    return all_combinations


def reverse_complement(text):
    """Find the reverse complement of a DNA string."""
    complement = {"A": "T", "T": "A", "C": "G", "G": "C"}
    return "".join([complement[x] for x in text[::-1]])


def dna_to_rna(text):
    """dna string to rna string"""
    import re

    return re.sub("T", "U", text)


def rna_to_dna(text):
    """rna string to dna string"""
    import re

    return re.sub("U", "T", text)


def find_all(pattern, text):
    i = text.find(pattern)
    while i != -1:
        yield i
        i = text.find(pattern, i + 1)


def get_all_amino_acid_candidates(dna, peptide):
    n = len(peptide) * 3

    rcdna = reverse_complement(dna)
    rna = dna_to_rna(dna)
    rcrna = dna_to_rna(rcdna)

    candidates = get_all_combinations(peptide)

    valid = []

    for cand in candidates:
        for index in find_all(cand, rna):
            valid.append(dna[index : index + n])
            continue
        for index in find_all(cand, rcrna):
            valid.append(reverse_complement(rcdna[index : index + n]))

    return valid


if __name__ == "__main__":

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    dna = inlines[0]
    peptide = inlines[1]

    res = get_all_amino_acid_candidates(dna, peptide)

    sys.stdout.write(rosalindprint(res))
