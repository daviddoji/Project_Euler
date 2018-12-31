#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  31 19:26:29 2018

@author: daviddoji

Solution to Project Euler problem 22

https://github.com/daviddoji/Project_Euler
"""


def compute():
    """
    Using names.txt, a 46K text file containing over five-thousand first names,
    begin by sorting it into alphabetical order. Then working out the
    alphabetical value for each name, multiply this value by its alphabetical
    position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
    COLIN would obtain a score of 938 × 53 = 49714.

    What is the total of all the name scores in the file?
    """
    with open('../files/Problem22.txt', 'r') as f:
        names = sorted(f.read().replace('"', '').split(','))

    result = 0
    for idx, name in enumerate(names, 1):
        result += sum(ord(c) - 64 for c in name) * idx
    return result


if __name__ == "__main__":

    print(compute())
