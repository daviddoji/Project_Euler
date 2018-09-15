#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  15 19:42:41 2018

@author: daviddoji

Solution to Project Euler problem 20

https://github.com/daviddoji/Project_Euler
"""

import math
def compute():
    """
    n! means n × (n − 1) × ... × 3 × 2 × 1
    
    For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
    and the sum of the digits in the number 10! is:
    3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
    
    Find the sum of the digits in the number 100!
    """
    fact = math.factorial(100)
    sum_digits = sum(int(digit) for digit in str(fact))
    
    return sum_digits 


if __name__ == "__main__":

    print(compute())
