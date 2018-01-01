#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 17:07:15 2018

@author: david
"""

import itertools
from math import sqrt, floor


# Returns the number of integers in the range [1, n] that divide n.
def num_divisors(n):
    end = floor(sqrt(n))
    divs = []
    for i in range(1, end + 1):
        if n % i == 0:
            divs.append(i)
    if end**2 == n:
        divs.pop()
    return 2*len(divs)


def compute():
    triangle = 0
    for i in itertools.count(1):
        # This is the ith triangle number, i.e. num = 1 + 2 + ... + i =
        # = i*(i+1)/2
        triangle += i
        if num_divisors(triangle) > 500:
            return str(triangle)


if __name__ == "__main__":

    print(compute())
