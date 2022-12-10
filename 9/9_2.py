#!/bin/python

from collections import defaultdict
import sys

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dir):
        if dir == "R": self.x += 1
        if dir == "U": self.y += 1
        if dir == "L": self.x -= 1
        if dir == "D": self.y -= 1

    def __repr__(self):
        return f"({self.x},{self.y})"

    def get_distance(self, other):
        return ((other.x - self.x), (other.y - self.y))

    def follow(self, other):
        d_x, d_y = self.get_distance(other)
        # print("follow self -> other:", self, other)
        # print("distance:", d_x, d_y)
        assert abs(d_x) < 3
        assert abs(d_y) < 3
        if abs(d_x) > 1:
            if d_x > 0:
                self.move("R")
            else:
                self.move("L")
            if d_y > 0:
                self.move("U")
            elif d_y < 0:
                self.move("D")
        elif abs(d_y) > 1:
            if d_y > 0:
                self.move("U")
            else:
                self.move("D")
            if d_x > 0:
                self.move("R")
            elif d_x < 0:
                self.move("L")
        # print("after follow self -> other:", self, other)

    def get_pos(self):
        return (self.x, self.y)

def plot_chain(chain, with_nums=False):
    match = False
    for y in range(min_y-2, max_y+2):
        for x in range(min_x-2, max_x+2):
            for i, node in enumerate(chain):
                node_x, node_y = node.get_pos()
                if node_x == x and node_y == y:
                    match = True
                    break
            if match:
                if with_nums:
                    sys.stdout.write(str(i))
                else:
                    sys.stdout.write("#")
                match = False
            else:
                sys.stdout.write(".")
        sys.stdout.write("\n")
    


chain = []
for _ in range(10):
    chain.append(Pos(0,0))

def visits_default():
    return 0

visits_tail = defaultdict(visits_default)
visits_tail[chain[-1].get_pos()] = 1
track_tail = [Pos(0, 0)]

max_x = -10
max_y = 10
min_x = -10
min_y = 10
print(min_x, max_x, min_y, max_y)
# plot_chain(chain)
linecount = 0
with open("input", "r") as f:
    for line in f:
        linecount += 1
        print(linecount)
        direction, distance = line.strip().split(" ")
        for _ in range(int(distance)):
            print("move HEAD:", direction)
            chain[0].move(direction)
            x, y = chain[0].get_pos()
            max_x = max(max_x, x)
            max_y = max(max_y, y)
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            # print("chain before follow:", chain)
            for i in range(len(chain)-1):
                # print("follow with chain element:", i+1, chain[i+1])
                chain[i+1].follow(chain[i])
            # print("chain after follow:", chain)
            print("TAIL:", chain[-1])
            visits_tail[chain[-1].get_pos()] += 1
            track_tail.append(Pos(*chain[-1].get_pos()))
            # plot_chain(chain, with_nums=True)

print("====")
print(len(visits_tail.keys()))
print("====")
# plot_chain(track_tail)
