#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  13 11:24:31 2018

@author: daviddoji

Solution to Project Euler problem 17

https://github.com/daviddoji/Project_Euler
"""


def num2letters(num):
    nums = {0: '', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
            11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
            15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen',
            19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty',
            50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty',
            90: 'ninety', 100: 'hundred', 1000: 'thousand'}

    if num <= 20:
        return len(nums[num])
    elif num < 100:
        tens, units = divmod(num, 10)
        return len(nums[tens * 10]) + num2letters(units)
    elif num < 1000:
        hundreds, rest = divmod(num, 100)
        if rest:
            return num2letters(hundreds) + len(nums[100]) + len('and') +\
                   num2letters(rest)
        else:
            return num2letters(hundreds) + len(nums[100])
    else:
        thousands, rest = divmod(num, 1000)
        return num2letters(thousands) + len(nums[1000])


def compute():
    """
    If the numbers 1 to 5 are written out in words: one, two, three, four,
    five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written
    out in words, how many letters would be used?

    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of "and" when writing out numbers is in compliance
    with British usage.
    """
    n = 1000
    letters = 0
    for num in range(1, n + 1):
        letters += num2letters(num)
    return letters


if __name__ == "__main__":

    print(compute())
