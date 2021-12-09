#PART TWO: https://adventofcode.com/2021/day/9
#DATE: 09/12/2021
#ANSWER: 1148965

from typing import ByteString
import numpy as np


with open("input.txt", "r") as file:
    x = file.readlines()

x = [i.rstrip() for i in x]

rows = len(x)
columns = len(x[0])

height_map = np.zeros((rows, columns), int)

for r, line in enumerate(x):
    for c, char in enumerate(line):
        height_map[r, c] = int(char)

low_points = []
adjacents = []

print(height_map)

for j in range(rows):
    for i in range(columns):
        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:
                if(row_offset == 0 and col_offset == 0):
                    continue
                if(row_offset == 0 or col_offset == 0):
                    r = j + row_offset
                    c = i + col_offset
                    if(r >= 0 and j + r < rows):
                        if(c >= 0 and c < columns):
                            adjacents.append((height_map[r, c], [r, c]))# (value , coordinates)
        
        adjacents.sort(key = lambda t: t[0])
        local_low_point = adjacents[0][0]
        if(local_low_point > height_map[j, i]):
            low_points.append((j, i))
        adjacents = []

basins_sizes = []

for p in low_points:
    open_list = []
    closed_list = []
    basin = []
    open_list.append(p)
    while(len(open_list)>0):
        chunk = open_list[0]
        j = chunk[0]
        i = chunk[1]
        for row_offset in [-1, 0, 1]:
            for col_offset in [-1, 0, 1]:
                if(row_offset == 0 and col_offset == 0):continue
                if(row_offset == 0 or col_offset == 0):
                    r = j + row_offset
                    c = i + col_offset
                    if(r >= 0 and r < rows):
                        if(c >= 0 and c < columns):
                            if(height_map[r, c]) < 9:
                                coords = (r, c)
                                if(not coords in open_list and not coords in closed_list):
                                    open_list.append(coords)
        
        if( not chunk in basin):
            basin.append(chunk)
        closed_list.append(chunk)
        open_list.remove(chunk)
    basins_sizes.append(len(basin))

largest_basins = sorted(basins_sizes, reverse=True)[:3]



print(np.prod(largest_basins))