#!/usr/bin/env python3

"""
A solution to a Rosalind bioinformatics problem

Problem Title: Find the Minimum Number of Coins Needed to Make Change
Rosalind ID: BA5A
URL: http://rosalind.info/problems/ba5a/
"""


def dpChangeMoney(money, coins):
    minnumcoins = (money + 1) * [0]
    for m in range(1, money + 1):
        minnumcoins[m] = m + 1  # basically the same as Inf since coins can't be <= 0
        for coin in coins:
            if m >= coin:
                if minnumcoins[m - coin] + 1 < minnumcoins[m]:
                    minnumcoins[m] = minnumcoins[m - coin] + 1
    return minnumcoins[money]


if __name__ == "__main__":

    import sys

    inlines = [x.strip("\n") for x in sys.stdin.readlines()]
    money = int(inlines[0])
    coins = [int(x) for x in inlines[1].split(",")]

    res = dpChangeMoney(money, coins)

    sys.stdout.write(str(res))
