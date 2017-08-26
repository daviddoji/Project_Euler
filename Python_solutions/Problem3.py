#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 18:09:31 2017

@author: daviddoji

Solution to Project Euler problem 3

https://github.com/daviddoji/Project_Euler
"""


def compute():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143 ?
    """
    n = 600851475143
    i = 2
    while i * i < n:
        while n % i == 0:
            n = n // i
        i = i + 1
    return n


if __name__ == "__main__":

    print(compute())
