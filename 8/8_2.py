#!/bin/python

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

    def get_dimensions(self):
        return (len(self.rows[0]), len(self.rows))

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
        
def viewing_distance(row, pos):
    # return scenic score for a row from pos
    tree_height = row[pos]
    dist_right = 0
    if pos != len(row):
        for x in range(pos+1, len(row)):
            dist_right += 1
            if row[x] >= tree_height:
                break
    dist_left = 0
    if pos != 0:
        for x in range(pos-1, -1, -1):
            dist_left += 1
            if row[x] >= tree_height:
                break
    return dist_right * dist_left
            

forest = Matrix()

with open("input", "r") as f:
    for line in f:
        row = list(map(int, list(line.strip())))
        forest.add_row(row)

# print(forest)

max_scenic_score = 0
width, height = forest.get_dimensions()
for y in range(height):
    for x in range(width):
        row = forest.get_row(y)
        col = forest.get_col(x)
        row_vd = viewing_distance(row, x)
        col_vd = viewing_distance(col, y)
        scenic_score = row_vd * col_vd
        max_scenic_score = max(max_scenic_score, scenic_score)

print(max_scenic_score)
