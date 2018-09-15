#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 19:20:56 2017

@author: daviddoji

Solution to Project Euler problem 4

https://github.com/daviddoji/Project_Euler
"""


def compute():
    """
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 x 99.
    Find the largest palindrome made from the product of two 3-digit numbers.
    """
    ans = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            k = i * j
            s = str(k)
            if s == s[::-1] and k > ans:
                ans = k
    return ans


if __name__ == "__main__":

    print(compute())
