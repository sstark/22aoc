#!/bin/python

from operator import add
obsidian = {}
min = -1
max = 21

def add_cube(obsidian, line):
    coord = tuple(map(int, line.split(",")))
    sides = 6
    for n in touching_neighours(obsidian, coord):
        sides -= 1
        obsidian[n] -= 1
    obsidian[coord] = sides

def neighbours(coord):
    for neigh in [(0,0,-1),(0,0,1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0)]:
        yield tuple(map(add, coord, neigh))

def touching_neighours(obsidian, coord):
    for neigh in neighbours(coord):
        if neigh in obsidian:
            yield neigh

def out_of_bounds(coord):
    for c in coord:
        if c < min or c > max:
            return True
    return False

# surrounding air minus the obsidian
air_hull = {(0, 0, 0): True}
# only the air molecules touching the obsidian
air_shell = {}

def expand_air():
    expanded_space = {}
    for air_molecule in air_hull:
        for neigh in neighbours(air_molecule):
            if neigh in air_hull:
                # already seen
                continue
            if neigh in obsidian:
                air_shell[air_molecule] = True
                # not air
                continue
            if out_of_bounds(neigh):
                continue
            expanded_space[neigh] = True
    return expanded_space

while True:
    try:
        next = input()
    except EOFError:
        break
    add_cube(obsidian, next)

while True:
    new = expand_air()
    if new:
        air_hull.update(new)
    else:
        break

sum = 0
for air_molecule in air_shell:
    for neigh in neighbours(air_molecule):
        if neigh in obsidian:
            sum += 1
print(sum)
