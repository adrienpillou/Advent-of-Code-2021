import numpy as np
import pprint

with open("input.txt") as file:
    x = [list(i) for i in file.read().split("\n")]

grid = np.matrix(x, int)

ROWS = grid.shape[0]
COLS = grid.shape[1]

nodes = dict()

for r in range(ROWS):
    for c in range(COLS):
        nodes[(r, c)] = [0, None] # Path weight, Parent

fixed_nodes = set()
start_node = (0, 0)
selected_node = start_node
fixed_nodes.add(start_node)

while(len(fixed_nodes) != len(nodes.keys())):
    r, c = selected_node
    w = nodes[selected_node][0]
    for ro in [-1, 0, 1]:
        for co in [-1, 0, 1]:
            if(abs(co) == abs(ro)):
                continue
            if(co == 0 and ro ==0):
                continue
            if(r + ro < 0 or r + ro >= ROWS):
                continue
            if(c + co < 0 or c + co >= COLS):
                continue
            
            neighbor_key = (r + ro, c + co)
            if(neighbor_key in fixed_nodes):
                continue

            neighbor_weight = grid[neighbor_key[0], neighbor_key[1]]
            if (w+neighbor_weight < nodes[neighbor_key][0] or nodes[neighbor_key][0] == 0):
                nodes[neighbor_key][0] = w + neighbor_weight
                nodes[neighbor_key][1] = selected_node
    
    fixed_nodes.add(selected_node)

    min_weight = 2**8
    for r in range(ROWS):
        for c in range(COLS):
            node_key = (r, c)
            if(nodes[node_key][0] == 0):
                continue
            if node_key in fixed_nodes:
                continue
            if(nodes[node_key][0] < min_weight):
                min_weight = nodes[node_key][0]
                selected_node = node_key

end_node_key = (ROWS-1, COLS-1)
print(nodes[end_node_key][0])

