#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  15 20:57:53 2018

@author: daviddoji

Solution to Project Euler problem 21

https://github.com/daviddoji/Project_Euler
"""


def sum_divisors(n):
    divs = []
    for i in range(1, n//2+1):
        if n % i == 0:
            divs.append(i)

    return sum(divs)


def compute():
    """
    Let d(n) be defined as the sum of proper divisors of n (numbers 
    less than n which divide evenly into n).
    If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable
    pair and each of a and b are called amicable numbers.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 
    44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 
    1, 2, 4, 71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.
    """
    n = 10000
    sum_amicable = 0
    for i in range(1, n):
        value = sum_divisors(i)
        if i != value and sum_divisors(value) == i:
            sum_amicable += i
    return sum_amicable


if __name__ == "__main__":

    print(compute())
