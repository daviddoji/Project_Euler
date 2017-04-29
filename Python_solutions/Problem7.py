#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 28 21:34:38 2017

@author: david

Solution to Project Euler problem 7

https://github.com/daviddoji/Project_Euler
"""

import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def compute():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
    we can see that the 6th prime is 13.

    What is the 10 001st prime number?

    """
    number = 2
    primeList = []
    while len(primeList) < 10001:
        if is_prime(number):
            primeList.append(number)
        number += 1
    ans = primeList[len(primeList)-1]
    return ans


if __name__ == "__main__":

    print(compute())
