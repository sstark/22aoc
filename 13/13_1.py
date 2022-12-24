#!/bin/python

tmp_data = []
data = []
with open("input", "r") as f:
    for i, line in enumerate(f):
        if line != "\n":
            tmp_data.append(eval(line.strip()))
        else:
            data.append(tuple(tmp_data))
            tmp_data = []

def both_int(a, b):
    return isinstance(a, int) and isinstance(b, int)

def get_items(pair):
    i = 0
    a, b = pair
    while True:
        try:
            p1 = a[i]
        except IndexError:
            p1 = None
        try:
            p2 = b[i]
        except IndexError:
            p2 = None
        if p1 == None and p2 == None:
            break
        i += 1
        yield (p1, p2)

def is_in_order(pair):
    for a, b in get_items(pair):
        if a == None:
            return True
        if b == None:
            return False
        if both_int(a, b):
            if a < b:
                return True
            elif a > b:
                return False
            else:
                continue
        ret = None
        if isinstance(a, int) and isinstance(b, list):
            ret = is_in_order(([a], b))
        if isinstance(a, list) and isinstance(b, int):
            ret = is_in_order((a, [b]))
        if isinstance(a, list) and isinstance(b, list):
            ret = is_in_order((a, b))
        if ret == None:
            continue
        else:
            return ret


sum = 0
for i, pair in enumerate(data):
    # print("#{}: {} -> {}".format(i+1, pair, is_in_order(pair)))
    if is_in_order(pair):
        sum += i+1
print(sum)
