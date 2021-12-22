

import numpy as np

with open("input.txt") as file:
    x = file.read().split("\n")

shape = (101, 101, 101)

grid = np.zeros(shape, dtype=int)

instructions = []

for line in x:
    state = line.split()[0]
    coordinates = line.split()[1]
    coordinates = [c for c in coordinates.split(",")]
    for i in range(len(coordinates)):
        coordinates[i] = coordinates[i][2:]
        coordinates[i] = [int(c)+50 for c in coordinates[i].split("..")]
    instructions.append((state, coordinates))


for state, coordinates in instructions[:20]:
    x_range = range(coordinates[0][0], coordinates[0][1]+1)
    y_range = range(coordinates[1][0], coordinates[1][1]+1)
    z_range = range(coordinates[2][0], coordinates[2][1]+1)
    for x in x_range:
        for y in y_range:
            for z in z_range:
                if state == "on":
                    grid[x, y, z] = 1
                elif state == "off":
                    grid[x, y, z] = 0

count = 0
for x in grid.flatten():
    count += x

print(count)