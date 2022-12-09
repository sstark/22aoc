#!/bin/python

from collections import defaultdict

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, dir):
        print("move", self, dir)
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
        print("self -> other:", self, other)
        print("distance:", d_x, d_y)
        if d_x > 1:
            self.move("R")
            self.y += d_y
        elif d_x < -1:
            self.move("L")
            self.y += d_y
        elif d_y > 1:
            self.move("U")
            self.x += d_x
        elif d_y < -1:
            self.move("D")
            self.x += d_x

    def get_pos(self):
        return (self.x, self.y)

tail = Pos(0,0)
head = Pos(0,0)

def visits_default():
    return 0
visits_head = defaultdict(visits_default)
visits_head[head.get_pos()] = 1
visits_tail = defaultdict(visits_default)
visits_tail[tail.get_pos()] = 1
track_head = [Pos(0, 0)]
track_tail = [Pos(0, 0)]


with open("input", "r") as f:
    for line in f:
        direction, distance = line.strip().split(" ")
        for _ in range(int(distance)):
            print("head")
            head.move(direction)
            visits_head[head.get_pos()] += 1
            track_head.append(head.get_pos())
            print("tail")
            tail.follow(head)
            visits_tail[tail.get_pos()] += 1
            track_tail.append(tail.get_pos())

for x in zip(track_head, track_tail):
    print(x)

print(len(visits_tail.keys()))
