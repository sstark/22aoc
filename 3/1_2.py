#!/bin/env python

import string

def get_priority(c):
    return string.ascii_letters.find(c)+1

def in_all(*args):
    # cast all arguments into sets and return one element of the intersection
    return set.intersection(*tuple(map(set, args))).pop()

def get_group_priorities():
    n = 0
    group = []
    for l in open('input', 'r'):
        l = l.strip()
        n += 1
        group.append(l)
        if n % 3 == 0 and n > 0:
            yield get_priority(in_all(*group))
            n = 0
            group = []

print(sum(get_group_priorities()))
