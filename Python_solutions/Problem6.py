#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 16:53:39 2017

@author: david

Solution to Project Euler problem 6

https://github.com/daviddoji/Project_Euler
"""


def compute():
    """
    The sum of the squares of the first ten natural numbers is,
    1^2 + 2^2 + ... + 10^2 = 385

    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)^2 = 55^2 = 3025

    Hence the difference between the sum of the squares of the first ten
    natural numbers and the square of the sum is 3025 − 385 = 2640.

    Find the difference between the sum of the squares of the first one
    hundred natural numbers and the square of the sum.

    """
    n = 100
    square_of_sum = sum(i for i in range(1, n+1))**2
    sum_squares = sum(i**2 for i in range(1, n+1))
    diff = square_of_sum - sum_squares
    return diff


if __name__ == "__main__":

    print(compute())
