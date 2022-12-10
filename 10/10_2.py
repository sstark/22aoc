#!/bin/python

import sys

class Clock:
    def __init__(self):
        self.cycles_done = 0
        self.in_cycle = False

    def start_cycle(self):
        assert self.in_cycle == False
        self.in_cycle = True

    def stop_cycle(self):
        assert self.in_cycle == True
        self.in_cycle = False
        self.cycles_done += 1
    
    def tick(self):
        self.start_cycle()
        self.stop_cycle()

class Cpu:
    def __init__(self, clock, crt):
        self.clock = clock
        self.current_op = ""
        self.last_op = ""
        self.reg_X = 1
        self.signal_strength = 0
        self.signal_strength_sum = 0
        self.crt = crt

    def start_cycle(self):
        self.clock.start_cycle()
        current_cycle = self.clock.cycles_done + 1
        if (current_cycle == 20) or (((current_cycle+20) % 40) == 0):
            self.signal_strength = current_cycle * self.reg_X
            # print("current_cycle:", current_cycle)
            # print("reg_X:", self.reg_X)
            # print("signal_strength:", self.signal_strength)
            self.signal_strength_sum += self.signal_strength

    def stop_cycle(self):
        self.crt.draw_pixel(self.reg_X, self.clock.cycles_done+1)
        self.clock.stop_cycle()

    def tick(self):
        self.start_cycle()
        self.stop_cycle()

    def noop(self):
        self.tick()
        self.last_op = "noop"

    def addx(self, i):
        self.current_op = "addx"
        self.tick()
        self.start_cycle()
        self.reg_X += i
        self.stop_cycle()
        self.current_op = ""
        self.last_op = "addx"

    def dump_info(self):
        print()
        print("cycles_done:", self.clock.cycles_done)
        print("in_cycle:", self.clock.in_cycle)
        print("current_op:", self.current_op)
        print("last_op:", self.last_op)
        print("reg_X:", self.reg_X)
        print("signal_strength_sum:", self.signal_strength_sum)
        print()

class Crt:
    def draw_pixel(self, reg_x, cycle):
        x = cycle % 40
        if abs(reg_x - x) < 2:
            sys.stdout.write("#")
        else:
            sys.stdout.write(".")
        if x == 0:
            sys.stdout.write("\n")


clock = Clock()
crt = Crt()
cpu = Cpu(clock, crt)

with open("input") as f:
    for line in f:
        op = line.strip().split(" ")
        instruction = op[0]
        
        if instruction == "noop":
            cpu.noop()

        elif instruction == "addx":
            operand = int(op[1])
            cpu.addx(operand)

cpu.dump_info()
