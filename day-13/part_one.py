#PART ONE: https://adventofcode.com/2021/day/13
#DATE: 13/12/2021
#ANSWER: 827

import numpy as np

import numpy as np

with open("input.txt") as file:
    x = file.read().split("\n")

dots = x[:x.index("")]

instructions = x[x.index("")+1:]
instructions = [i.split()[-1] for i in instructions]

for i in range(len(dots)):
    dots[i] = [int(dots[i].split(",")[0]), int(dots[i].split(",")[1])]

instruction = instructions[0]

value = int(instruction.split("=")[-1])

for i in range(len(dots)):
    if(dots[i][0] >= value):
        dx = dots[i][0] - value
        dots[i][0] = value - dx

dots_set = set()
for d in dots:
    dots_set.add(tuple(d))
print(len(dots_set))
