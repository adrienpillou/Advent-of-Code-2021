#PART TWO: https://adventofcode.com/2021/day/5
#DATE: 05/12/2021
#ANSWER: 

from utils import *
import numpy as np

with open("input.txt", "r") as file:
    x = file.readlines()

x = [i.rstrip() for i in x]

vents = []
for i in x:
    start_point = i.split("->")[0]
    end_point = i.split("->")[1]
    segment = Segment()
    segment.x1 = int(start_point.split(",")[0])
    segment.y1 = int(start_point.split(",")[1])
    segment.x2 = int(end_point.split(",")[0])
    segment.y2 = int(end_point.split(",")[1])
    vents.append(segment)

shape = (1000, 1000)
diagram = np.zeros(shape, int)

for v in vents:
    xdir = v.x2 - v.x1
    ydir = v.y2 - v.y1
    max_dir = max([abs(xdir), abs(ydir)])
    xdir = xdir / max_dir
    ydir = ydir / max_dir
    steps = max_dir

    c = v.x1
    r = v.y1

    for n in range(steps+1):
        diagram[r, c] += 1
        r += int(ydir)
        c += int(xdir)

print(np.count_nonzero(diagram > 1))