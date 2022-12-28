#!/bin/python

from itertools import starmap
from operator import add
obsidian = {}

def add_cube(obsidian, line):
    coord = tuple(map(int, line.split(",")))
    sides = 6
    for n in touching_neighours(obsidian, coord):
        sides -= 1
        obsidian[n] -= 1
    obsidian[coord] = sides

def tuple_add(t1, t2):
    return tuple(map(add, t1, t2))

def touching_neighours(obsidian, coord):
    neighbour_locations = [(0,0,-1),(0,0,1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0)]
    for n in neighbour_locations:
        neigh_coord = tuple_add(coord, n)
        if neigh_coord in obsidian:
            yield neigh_coord

while True:
    try:
        next = input()
    except EOFError:
        break
    add_cube(obsidian, next)

print(sum(obsidian.values()))
