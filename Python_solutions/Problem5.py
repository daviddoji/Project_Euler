#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 23 15:56:08 2017

@author: david

Solution to Project Euler problem 5

https://github.com/daviddoji/Project_Euler
"""

import math

# The lcm of two natural numbers x and y is given by:
#def lcm(x, y):
#    return x * y // math.gcd(x, y)
# It is possible to compute the LCM of more than two numbers by iteratively
# computing the lcm of two numbers, i.e.
# lcm(a, b, c) = lcm(a, lcm(b, c))

def compute():
    """
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?
    """
    ans = 1
    for i in range(1, 21):
        ans *= i // math.gcd(i, ans)
    return ans


if __name__ == "__main__":

    print(compute())