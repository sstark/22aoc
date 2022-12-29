#!/bin/python

from operator import add
obsidian = {}
min = -1
max = 21

def add_cube(obsidian, line):
    coord = tuple(map(int, line.split(",")))
    sides = 6
    for n in touching_neighours(obsidian, coord):
        # print("{} touches {}".format(coord, n))
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

def out_of_bounds(coord):
    for c in coord:
        if c < min or c > max:
            return True
    return False

air_hull = {(0, 0, 0): True}
air_shell = {}
def expand_air():
    neighbour_locations = [(0,0,-1),(0,0,1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0)]
    expanded_space = {}
    for air_molecule in air_hull:
        for neigh in neighbour_locations:
            neigh_coord = tuple_add(air_molecule, neigh)
            if neigh_coord in air_hull:
                # already seen
                continue
            if neigh_coord in obsidian:
                air_shell[air_molecule] = True
                # not air
                continue
            if out_of_bounds(neigh_coord):
                continue
            expanded_space[neigh_coord] = True
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
neighbour_locations = [(0,0,-1),(0,0,1),(0,-1,0),(0,1,0),(-1,0,0),(1,0,0)]
for air_molecule in air_shell:
    for neigh in neighbour_locations:
        neigh_coord = tuple_add(air_molecule, neigh)
        if neigh_coord in obsidian:
            sum += 1
print(sum)


# for k, v in air_shell.items():
#     print(k, v)
