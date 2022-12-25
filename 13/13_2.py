#!/bin/python

class Packet:
    def __init__(self, l):
        self.data = l

    def __both_int(self, a, b):
        return isinstance(a, int) and isinstance(b, int)
    
    def __getitem__(self, i):
        return self.data[i]

    def __len__(self):
        return len(self.data)

    def __get_items(self, pair):
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
            # print(i)
            if p1 == None and p2 == None:
                break
            i += 1
            yield (p1, p2)

    def __lt__(self, other):
        for a, b in self.__get_items((self.data, other)):
            if a == None:
                return True
            if b == None:
                return False
            if self.__both_int(a, b):
                if a < b:
                    return True
                elif a > b:
                    return False
                else:
                    continue
            if isinstance(a, int) and isinstance(b, list):
                ret = Packet([a]) < Packet(b)
                if ret == None:
                    continue
                else:
                    return ret
            if isinstance(a, list) and isinstance(b, int):
                ret = Packet(a) < Packet([b])
                if ret == None:
                    continue
                else:
                    return ret
            if isinstance(a, list) and isinstance(b, list):
                ret = Packet(a) < Packet(b)
                if ret == None:
                    continue
                else:
                    return ret
            return len(a) < len(b)

    def __repr__(self):
        return "Packet<{}>".format(str(self.data))


P2 = Packet([[2]])
P6 = Packet([[6]])
data = [P2, P6]
with open("input", "r") as f:
    for line in f:
        if line != "\n":
            data.append(Packet(eval(line.strip())))

data = sorted(data)
print((data.index(P2)+1)*(data.index(P6)+1))
