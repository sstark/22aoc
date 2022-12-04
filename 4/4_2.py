#!/bin/python

class Sections():

    def __init__(self, s):
        a, b = s.split("-")
        self.id_lo, self.id_hi = int(a), int(b)

    def contains(self, s):
        return s.id_lo >= self.id_lo and s.id_hi <= self.id_hi

    def in_range(self, i):
        return i <= self.id_hi and i >= self.id_lo

    def overlaps(self, s):
        return self.in_range(s.id_hi) or self.in_range(s.id_lo)

    def __repr__(self):
        return f"{self.id_lo}-{self.id_hi}"

class Pair():

    def __init__(self, s):
        super().__init__()
        a, b = s.split(",")
        self.p1 = Sections(a)
        self.p2 = Sections(b)

    def check(self):
        return self.p1.overlaps(self.p2) or self.p2.overlaps(self.p1)

    def __repr__(self):
        return f"{self.p1},{self.p2}"

s = 0
with open("input", "r") as f:
    for l in f:
        p = Pair(l.strip())
        if p.check(): s+=1

print(s)
