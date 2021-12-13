#PART TWO: https://adventofcode.com/2021/day/13
#DATE: 13/12/2021
#ANSWER: EAHKRECP

import numpy as np

with open("input.txt") as file:
    x = file.read().split("\n")

dots = x[:x.index("")]

instructions = x[x.index("")+1:]
instructions = [i.split()[-1] for i in instructions]

for i in range(len(dots)):
    dots[i] = [int(dots[i].split(",")[0]), int(dots[i].split(",")[1])]

def print_dots():
    rows = 0
    cols = 0

    for d in dots:
        if d[1]>rows:
            rows = d[1]
        if d[0]>cols:
            cols = d[0]
    
    shape = (rows+1, cols+1)
    grid = np.chararray(shape, unicode=True)
    grid.fill("░")

    for d in dots:
        grid[d[1], d[0]] = "█"

    print("\n")
    for row in grid:
        print("".join(row))

for instruction in instructions:
    value = int(instruction.split("=")[-1])
    if "x" in instruction:
        for i in range(len(dots)):
            if(dots[i][0] >= value):
                dx = dots[i][0] - value
                dots[i][0] = value - dx

    elif "y" in instruction:
        for i in range(len(dots)):
            if(dots[i][1] >= value):
                dy = dots[i][1] - value
                dots[i][1] = value - dy
print_dots()
