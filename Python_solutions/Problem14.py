#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 20:32:56 2018

@author: david

Solution to Project Euler problem 14

https://github.com/daviddoji/Project_Euler
"""


def getChainLength(n, terms):
    length = 0
    while n != 1:
        if n in terms:
            length += terms[n]
            break
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        length += 1
    return length


def compute():
    """"
    The following iterative sequence is defined for the set of positive
    integers:

    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

    Using the rule above and starting with 13, we generate the following
    sequence:

    13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

    It can be seen that this sequence (starting at 13 and finishing at 1)
    contains 10 terms. Although it has not been proved yet (Collatz Problem),
    it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.
    """
    limit = 1000000
    longest = 0
    score = 0
    terms = dict()
    for i in range(1, limit):
        terms[i] = getChainLength(i, terms)
        if terms[i] > score:
            score = terms[i]
            longest = i
    return longest


if __name__ == "__main__":

    print(compute())
