#!/bin/python

from collections import defaultdict

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


def first_is_biggest(l):
    # return True if the first element in list is the biggest
    if len(l) == 1:
        return True
    first = l[0]
    # print("fib:", l)
    for e in l[1:]:
        if e >= first:
            return False
    return True

def get_visible_trees(row):
    vis_from_r = []
    vis_from_l = []
    for i in range(len(row)):
        if first_is_biggest(row[i:]):
            vis_from_r.append(i)
    row_backwards = row[::-1]
    for i in range(len(row)):
        if first_is_biggest(row_backwards[i:]):
            vis_from_l.append(len(row_backwards)-i-1)
    vis_from_l.reverse()
    return set(vis_from_l + vis_from_r)


forest = Matrix()

with open("input", "r") as f:
    for line in f:
        row = list(map(int, list(line.strip())))
        forest.add_row(row)

# print(forest)

visible_trees = defaultdict()

for row_count, row in enumerate(forest.get_rows()):
    # print("row:", row_count)
    vis_rows = get_visible_trees(row)
    for x in vis_rows:
        visible_trees[(x, row_count)] = True
    print(vis_rows)

vis_col = 0
for col_count, col in enumerate(forest.get_cols()):
    # print("col:", col_count)
    vis_cols = get_visible_trees(col)
    for y in vis_cols:
        visible_trees[(col_count, y)] = True
    print(vis_cols)

print(len(visible_trees))
