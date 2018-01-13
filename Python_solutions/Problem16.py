#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  13 11:11:45 2018

@author: daviddoji

Solution to Project Euler problem 16

https://github.com/daviddoji/Project_Euler
"""


def compute():
    """
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

    What is the sum of the digits of the number 2^1000?
    """
    n = 1000
    number = 2**n
    sum_digits = sum(int(digit) for digit in str(number))

    return sum_digits


if __name__ == "__main__":

    print(compute())
