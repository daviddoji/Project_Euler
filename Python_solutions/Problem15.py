#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 20:56:26 2018

@author: david

Solution to Project Euler problem 15

https://github.com/daviddoji/Project_Euler
"""

from math import factorial


def compute():
    """
    Starting in the top left corner of a 2×2 grid, and only being able to
    move to the right and down, there are exactly 6 routes to the bottom
    right corner.

    How many such routes are there through a 20×20 grid?
    """
    n = 20
    return int(factorial(2*n) / (factorial(n) * factorial(2*n - n)))


if __name__ == "__main__":

    print(compute())
