#!/bin/python

# 498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9

from itertools import pairwise
from collections import defaultdict
import sys

outlet_coord = (500, 0)
outlet = "+"
air = "."
wall = "#"
sand = "o"

cave = defaultdict(lambda: air)
cave[outlet_coord] = outlet

def ranch(i, j):
    if i <= j:
        return range(i, j+1)
    if i > j:
        return range(i, j-1, -1)

def draw(pair):
    a, b = pair
    ax, ay = map(int, a.split(","))
    bx, by = map(int, b.split(","))
    if ax == bx: # vertical
        for y in ranch(ay, by):
            cave[(ax, y)] = wall
    if ay == by: # horizontal
        for x in ranch(ax, bx):
            cave[(x, ay)] = wall

def plot_cave(cave):
    for y in ranch(min_y, max_y):
        for x in ranch(min_x, max_x):
            sys.stdout.write(cave[(x, y)])
        print()

def drop_sand(coord):
    x, y = coord
    down = (x, y+1)
    left = (x-1, y+1)
    right = (x+1, y+1)
    for next in [down, left, right]:
        if cave[next] == air:
            return drop_sand(next)
    return coord
    

with open("input") as f:
    for l in f:
        for pair in pairwise(l.strip().split(" -> ")):
            draw(pair)

all_x = sorted([e[0] for e in cave])
all_y = sorted([e[1] for e in cave])
min_x = all_x[0]
max_x = all_x[-1]
min_y = all_y[0]
max_y = all_y[-1]

# lame
draw((f"{min_x-1000},{max_y+2}", f"{max_x+1000},{max_y+2}"))
all_x = sorted([e[0] for e in cave])
all_y = sorted([e[1] for e in cave])
min_x = all_x[0]
max_x = all_x[-1]
min_y = all_y[0]
max_y = all_y[-1]

plot_cave(cave)
i = 0
while True:
    next = drop_sand(outlet_coord)
    i += 1
    if next == outlet_coord:
        break
    cave[next] = sand
plot_cave(cave)
print(i)
