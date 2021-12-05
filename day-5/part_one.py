#PART ONE: https://adventofcode.com/2021/day/5
#DATE: 05/12/2021
#ANSWER: 6225

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
    
    # Avoid diagonal vents
    if(segment.x1 == segment.x2) or (segment.y1 == segment.y2): 
        vents.append(segment)

shape = (1000, 1000)
diagram = np.zeros(shape, int)

for v in vents:
    xdir = v.x2 - v.x1
    ydir = v.y2 - v.y1

    if(xdir != 0):
        steps = abs(xdir)
        xdir = xdir / steps
    elif(ydir != 0):
        steps = abs(ydir)
        ydir = ydir / steps
    
    c = v.x1
    r = v.y1

    for n in range(steps+1):
        diagram[r, c] += 1
        r += int(ydir)
        c += int(xdir)

print(np.count_nonzero(diagram > 1))

