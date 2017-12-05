#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 23:05:24 2017

@author: david

Solution to Project Euler problem 9

https://github.com/daviddoji/Project_Euler
"""

import math


# Tests whether the given integer is a prime number
def is_prime(x):
    if x <= 1:
        return False
    elif x <= 3:
        return True
    elif x % 2 == 0:
        return False
    else:
        for i in range(3, math.sqrt(x) + 1, 2):
            if x % i == 0:
                return False
    return True


# Returns a list of True and False indicating whether each number is prime.
# For 0 <= i <= n, result[i] is True if i is a prime number, False otherwise.
def list_primality(n):
    # Sieve of Eratosthenes
    result = [True] * (n + 1)
    result[0] = result[1] = False
    for i in range(int(math.sqrt(n) + 1)):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


# Returns all the prime numbers less than or equal to n, in ascending order
# For example: listPrimes(97) = [2, 3, 5, 7, 11, ..., 83, 89, 97].
def list_primes(n):
    return [i for (i, isprime) in enumerate(list_primality(n)) if isprime]


def compute():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

    Find the sum of all the primes below two million.
    """
    ans = sum(list_primes(1999999))
    return ans


#sieve = [True] * 2000000    # Sieve is faster for 2M primes
# 8
# 9 def mark(sieve, x):
#10     for i in xrange(x+x, len(sieve), x):
#11         sieve[i] = False
#12
#13 for x in xrange(2, int(len(sieve) ** 0.5) + 1):
#14     if sieve[x]: mark(sieve, x)
#15
#16 print sum(i for i in xrange(2, len(sieve)) if sieve[i])



if __name__ == "__main__":

    print(compute())
