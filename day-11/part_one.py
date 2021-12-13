#PART ONE: https://adventofcode.com/2021/day/11
#DATE: 11/12/2021
#ANSWER: 1741

import numpy as np

with open("input.txt") as file:
    x = file.readlines()

x = [i.rstrip() for i in x]

for i, line in enumerate(x):
    x[i] = list(line)

grid = np.matrix(x, int)

flashed_dumbos = []

step_limit = 100

def flash(g, j, i):
    rows = g.shape[0]
    columns = g.shape[1]
    flashed_dumbos.append((j, i))
    for ro in [-1, 0, 1]:
        for co in [-1, 0, 1]:
            if(co == 0 and ro == 0):
                continue
            if(j + ro >= 0 and j + ro < rows):
                if(i + co >= 0 and i + co < columns):
                    if not (j+ro, i+co) in flashed_dumbos:
                        g[j+ro, i+co] += 1
    
def step():
    global grid
    next_grid = grid.copy()

    flashed_dumbos.clear()

    shape = grid.shape
    rows = shape[0]
    columns = shape[1]

    flash_count = 0
    for j in range(rows):
        for i in range(columns):
            next_grid[j, i] += 1

    while(np.count_nonzero(next_grid > 9) > 0):
        flashing_dumbos = []
        for r in range(rows):
            for c in range(columns):
                if(next_grid[r, c] > 9):
                    flashing_dumbos.append((r,c))
        for d in flashing_dumbos:
            if(d in flashed_dumbos):
                continue
            dumbo_row, dumbo_column = d
            next_grid[dumbo_row, dumbo_column] = 0
            flash(next_grid, dumbo_row, dumbo_column)
            flash_count += 1

    grid = next_grid
    return flash_count

total_flashes = 0

for s in range(step_limit):
    total_flashes += step()
print(total_flashes)
