#PART ONE: https://adventofcode.com/2021/day/9
#DATE: 09/12/2021
#ANSWER: 417

import numpy as np

def calculate_risk(points):
    return sum([1 + v for v in points])

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
                if(row_offset == 0 and col_offset == 0):continue
                if(row_offset == 0 or col_offset == 0):
                    if(j + row_offset >= 0 and j + row_offset < rows):
                        if(i + col_offset >= 0 and i + col_offset < columns):
                            adjacents.append(height_map[j + row_offset,i + col_offset])
        
        adjacents.sort()
        local_low_point = adjacents[0]
        if(local_low_point > height_map[j, i]):
            low_points.append(height_map[j, i])
        adjacents = []

print(len(low_points), calculate_risk(low_points))


            

