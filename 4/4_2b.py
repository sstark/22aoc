#!/bin/python

# This is slow, and it is kind of a cheat

from sympy import Interval

s = 0
with open("input", "r") as f:
    for l in f:
        a, b = l.strip().split(",")
        i1 = Interval(*map(int, a.split("-")))
        i2 = Interval(*map(int, b.split("-")))
        if not i1.is_disjoint(i2):
            s += 1

print(s)
