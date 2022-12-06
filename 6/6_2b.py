#!/bin/python

from itertools import groupby

class RingBuf():
    def __init__(self, size):
        self.buf = []
        self.size = size
        self.count = 0

    def put(self, e):
        self.buf.append(e)
        self.count += 1
        if len(self.buf) > self.size:
            self.buf.pop(0)

    def check_diff(self):
        if len(self.buf) == self.size:
            return len(set(self.buf)) == len(self.buf)
        else:
            return False

    def check_diff2(self):
        if len(self.buf) != self.size:
            return False
        x = sorted(self.buf)
        u = []
        for k, _ in groupby(x):
            u.append(k)
        return len(u) == len(self.buf)

    def check_diff3(self):
        if len(self.buf) != self.size:
            return False
        for i, n in enumerate(self.buf):
            for m in self.buf[i+1:]:
                if n == m:
                    return False
        return True

r = RingBuf(14)
with open("input", "r") as f:
    for c in f.read():
        if c != '\n':
            r.put(c)
            if r.check_diff3():
                print(r.count)
                break
