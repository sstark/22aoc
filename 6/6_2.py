#!/bin/python

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
            

r = RingBuf(14)
with open("input", "r") as f:
    for c in f.read():
        if c != '\n':
            r.put(c)
            if r.check_diff():
                print(r.count)
                break
