#!/bin/python

import queue
import inspect

class Monkey:
    # data is an array of strings
    def __init__(self, data):
        self.items = queue.Queue(100)
        for item in self.__parse_value(data[1]).split(", "):
            self.items.put(int(item))
        self.op = self.__parse_op(data[2])
        self.test = int(self.__parse_value(data[3]).split(" ")[2])
        self.test_true = int(self.__parse_value(data[4]).split(" ")[3])
        self.test_false = int(self.__parse_value(data[5]).split(" ")[3])
        self.inspection_count = 0

    def __parse_value(self, s):
        return s.split(":")[1].strip()

    def __parse_op(self, s):
        op_expr = self.__parse_value(s).split(" ")
        op = op_expr[3]
        operand = op_expr[4]
        if op == "+":
            if operand == "old":
                def op_func(x): return x + x
            else:
                def op_func(x): return x + int(operand)
        if op == "*":
            if operand == "old":
                def op_func(x): return x * x
            else:
                def op_func(x): return x * int(operand)
        return op_func

    def info(self):
        print("items:", self.items.qsize())
        print("items:", self.items.queue)
        print("op:", inspect.getsource(self.op))
        print("test:", self.test)
        print("test_true:", self.test_true)
        print("test_false:", self.test_false)
        print("inspection_count:", self.inspection_count)
        print("###################")

    def do_test(self, item):
        if (item % self.test) == 0:
            return self.test_true
        else:
            return self.test_false

    def process(self, troop):
        items_left = not self.items.empty()
        while items_left:
            try:
                item = self.items.get_nowait()
                item = self.op(item)
                item = item // 3
                next_monkey = self.do_test(item)
                print(item, "->", next_monkey)
                troop[next_monkey].items.put_nowait(item)
                self.inspection_count += 1
            except queue.Empty:
                items_left = False

def troop_info(troop):
    for i, monkey in enumerate(troop):
        print("########## Monkey", i)
        monkey.info()

def play_round(troop):
    for i, monkey in enumerate(troop):
        print("monkey", i)
        monkey.process(troop)

monkey_troop = []

read_monkey_data = False
monkey_data = []
with open("input", "r") as f:
    for line in f:
        if line.startswith("Monkey"):
            read_monkey_data = True
        if read_monkey_data:
            monkey_data.append(line.strip())
        if line.strip() == "":
            read_monkey_data = False
            monkey_troop.append(Monkey(monkey_data))
            monkey_data = []
    monkey_troop.append(Monkey(monkey_data))

# troop_info(monkey_troop)
for _ in range(20):
    play_round(monkey_troop)

troop_info(monkey_troop)

activity = [x.inspection_count for x in monkey_troop]
activity.sort()
monkey_business = activity[-2] * activity[-1]
print(monkey_business)
