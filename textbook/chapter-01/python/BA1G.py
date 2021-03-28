#!/usr/bin/env python3

"""
A solution to a ROSALIND bioinformatics problem.

Problem Title: Compute the Hamming Distance Between Two Strings
Rosalind ID: BA1G
URL: http://rosalind.info/problems/ba1g
"""


def HammingDistance(p, q):
    """Computes the hamming distance between strings p and q"""
    if len(p) != len(q):
        return -1

    dist = 0
    for first, second in zip(p, q):
        if first != second:
            dist = dist + 1

    return dist


if __name__ == "__main__":

    #    p = "GGGCCGTTGGT"
    #    q = "GGACCGTTGAC"
    #    print(HammingDistance(p,q))

    with open("../data/rosalind_ba1g.txt", "r") as myfile:
        p = myfile.readline().replace("\n", "")
        q = myfile.readline().replace("\n", "")

    text_file = open("./out/rosalind_ba1g.txt", "w")
    text_file.write(str(HammingDistance(p, q)))
    text_file.close()
