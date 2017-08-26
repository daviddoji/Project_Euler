#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 22:06:19 2017

@author: david

Solution to Project Euler problem 9

https://github.com/daviddoji/Project_Euler
"""


def compute():
    """
    A Pythagorean triplet is a set of three natural numbers, a < b < c,
    for which a^2 + b^2 = c^2

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc.
    """
    upper_limit = 1000
    for a in range(1, upper_limit + 1):
        for b in range(a + 1, upper_limit + 1):
            c = upper_limit - a - b
            if a * a + b * b == c * c:
                # It is now implied that b < c, because we have a > 0
                return a * b * c


if __name__ == "__main__":

    print(compute())
