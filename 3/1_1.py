#!/bin/env python

import string

def get_priority(c):
    return string.ascii_letters.find(c)+1

def in_all(*args):
    # cast all arguments into sets and return one element of the intersection
    return set.intersection(*tuple(map(set, args))).pop()

def get_item_priorities():
    for l in open('input', 'r'):
        l = l.strip()
        assert len(l) % 2 == 0
        cpts = (l[:len(l)//2], l[len(l)//2:])
        assert len(cpts[0]) == len(cpts[1])
        item = in_all(*cpts)
        yield get_priority(item)

print(sum(get_item_priorities()))
