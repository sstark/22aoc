#!/bin/python

from string import ascii_letters
import sys
from heapq import heapify, heappush, heappop
from functools import total_ordering

class Matrix:

    def __init__(self):
        self.rows = []

    def add_row(self, row):
        self.rows.append(row)

    def __repr__(self):
        out = []
        for row in self.rows:
            out.append("".join(map(str, row)))
        return "\n".join(out)

    def get_rows(self):
        for row in self.rows:
            yield row

    def get_cols(self):
        for i in range(len(self.rows[0])):
            yield [x[i] for x in self.rows]

    def get_row(self, y):
        return self.rows[y]

    def get_col(self, x):
        return [row[x] for row in self.rows]

    def get_dimensions(self):
        return (len(self.rows[0]), len(self.rows))

    def get_val(self, x, y):
        return self.rows[y][x]

    def get_adjacent(self, x, y):
        size_x, size_y = self.get_dimensions()
        if x > 0:
            yield Node(self.get_val(x-1, y), x-1, y)
        if y > 0:
            yield Node(self.get_val(x, y-1), x, y-1)
        if x < size_x-1:
            yield Node(self.get_val(x+1, y), x+1, y)
        if y < size_y-1:
            yield Node(self.get_val(x, y+1), x, y+1)


@total_ordering
class Node():

    def __init__(self, letter, x, y):
        self.letter = letter
        self.dist = sys.maxsize
        self.height = ascii_letters.index(letter)
        if letter == "S":
            self.height = 0
        if letter == "E":
            self.height = ascii_letters.index('z')
            # change for #2
            self.dist = 0
        self.coord = (x, y)
        self.neighbours = {}
        self.parent = None

    def __repr__(self):
        out = "Node {} h{}: {} dist({}) Neighbours:\n\t{}\n".format(
            self.letter,
            self.height,
            str(self.coord),
            str(self.dist),
            self.neighbours
        )
        return out

    def add_neighbour(self, node, weight=1):
        self.neighbours[node] = weight 

    def get_neighours(self):
        return self.neighbours.keys()

    def __eq__(self, other):
        return self.dist == other.dist

    def __lt__(self, other):
        return self.dist < other.dist


class Graph:
    def __init__(self):
        self.nodes = {}

    def add_node(self, letter, x, y):
        new_node = Node(letter, x, y)
        self.nodes[(x, y)] = new_node
        return new_node

    def get_node(self, x, y):
        return self.nodes[(x, y)]

    def add_edge(self, from_xy, to_xy, weight=1):
        self.nodes[from_xy].add_neighbour(to_xy, weight)

    def __repr__(self):
        return "\n".join([str(x) for x in self.nodes.values()])

def in_queue(heap, node):
    for n in heap:
        if n.coord == node.coord:
            return True
    return False

graph = Graph()
topo = Matrix()
heap = []
heapify(heap)

print("load topo")
with open("input", "r") as f:
    for line in f:
        topo.add_row(line.strip())


print("make graph")
size_x, size_y = topo.get_dimensions()
for y in range(size_y):
    for x in range(size_x):
        new_node = graph.add_node(topo.get_val(x, y), x, y)
        for adj in topo.get_adjacent(x, y):
            # change for #2
            diff = graph.get_node(x, y).height - adj.height
            if diff <= 1:
                graph.add_edge((x, y), adj.coord)
                if not in_queue(heap, new_node):
                    heappush(heap, new_node)


# print(topo)
# print(graph)
# print(heap)

new_dist = 0
print("find shortest path")
while heap:
    node = heappop(heap)
    # change for #1
    if node.letter == "a" or node.letter == "S":
        print("found", node.letter)
        print(node.dist)
        break
    for neigh in node.neighbours:
        neigh_obj = graph.get_node(*neigh)
        if in_queue(heap, neigh_obj):
            new_dist = node.dist + 1
            if new_dist < neigh_obj.dist:
                neigh_obj.dist = new_dist
                neigh_obj.parent = node
                heapify(heap)
