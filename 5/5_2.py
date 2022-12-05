#!/bin/python

class Crates():
    def __init__(self, st):
        self.crates = st

    def get_last(self):
        return self.crates[-1]

    def pop(self):
        return self.crates.pop()

    def pop_mult(self, count):
        ret = self.crates[-count:]
        for _ in range(count):
            self.crates.pop()
        return ret

    def push(self, n):
        self.crates.append(n)

    def push_mult(self, l):
        self.crates.extend(l)

    def __repr__(self):
        return f"{self.crates}"


class CrateManager():
    def __init__(self, piles):
        self.stacks = []
        for s in piles:
            c = Crates(list(s))
            self.stacks.append(c)

    def move_one(self, fr, to):
        self.stacks[to].push(self.stacks[fr].pop())

    def move_mult(self, count, fr, to):
        self.stacks[to].push_mult(self.stacks[fr].pop_mult(count))

    def move(self, count, fr, to):
        # move 8 from 3 to 2
        for _ in range(count):
            self.move_one(fr, to)

    def __repr__(self):
        return f"{self.stacks}"


STACKS_INIT = [
    "HBVWNMLP",
    "MQH",
    "NDBGFQML",
    "ZTFQMWG",
    "MTHP",
    "CBMJDHGT",
    "MNBFVR",
    "PLHMRGS",
    "PDBCN",
]

STACKS_INIT_TEST = [
    "ZN", "MCD", "P"
]

cm = CrateManager(STACKS_INIT)
print(cm)
with open("input", "r") as f:
    for l in f:
        if l.startswith("move"):
            l = l.split(" ")
            cnt = int(l[1])
            fr = int(l[3]) - 1
            to = int(l[5]) - 1
            cm.move_mult(cnt, fr, to)

print(cm)
l = []
for s in cm.stacks:
    l.append(s.get_last())
print("".join(l))
