#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  13 11:24:31 2018

@author: daviddoji

Solution to Project Euler problem 19

https://github.com/daviddoji/Project_Euler
"""

import datetime

def compute():
    """
    You are given the following information, but you may prefer to do some
    research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September, April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century
    unless it is divisible by 400.

    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?
    """
    sundays = 0
    for y in range(1901, 2001):
        for m in range (1, 13):
            if datetime.date(y, m, 1).weekday() == 6:
                sundays += 1
    return sundays


if __name__ == "__main__":

    print(compute())
