#!/bin/python

from operator import add
from collections import deque
obsidian = {}
min = -1
max = 21

def add_cube(obsidian, line):
    obsidian[tuple(map(int, line.split(",")))] = True

def neighbours(coord):
    for neigh in [(0,0,-1),(0,0,1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0)]:
        yield tuple(map(add, coord, neigh))

def out_of_bounds(coord):
    for c in coord:
        if c < min or c > max:
            return True
    return False

def air_shell(obsidian):
    '''return coordinates of the air layer around the obsidian'''
    checked = {}
    shell = {}
    q = deque([(0,0,0)])
    while True:
        try:
            next = q.popleft()
        except IndexError:
            break
        if next in checked:
            continue
        else:
            checked[next] = True
        if out_of_bounds(next):
            continue
        for neigh in neighbours(next):
            if neigh in obsidian:
                shell[next] = True
            else:
                q.append(neigh)
    return shell


# build up obsidian from input
while True:
    try:
        add_cube(obsidian, input())
    except EOFError:
        break

sum = 0
for air_molecule in air_shell(obsidian):
    for neigh in neighbours(air_molecule):
        sum += neigh in obsidian
print(sum)
