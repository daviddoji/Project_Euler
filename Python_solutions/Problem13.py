#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 18:39:28 2018

@author: david

Solution to Project Euler problem 13

https://github.com/daviddoji/Project_Euler
"""


def compute():
    """
    Work out the first ten digits of the sum of the following one-hundred
    50-digit numbers.
    """
    # Problem13.txt is a file with the number as it is displayed on the
    # problem description
    with open("Problem13.txt", "r") as f:
        num = f.readlines()
        result = 0
        for line in num:
            result += int(line)
    return str(result)[:10]


if __name__ == "__main__":

    print(compute())
