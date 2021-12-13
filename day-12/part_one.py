#PART ONE: https://adventofcode.com/2021/day/12
#DATE: 12/12/2021
#ANSWER: 4707

from collections import defaultdict

with open("input.txt") as file:
    x = file.read().strip()
data = [i.split("-") for i in x.split("\n")]

adjacency = defaultdict(list)

for a, b in data:
    adjacency[a].append(b)
    adjacency[b].append(a)


path_count = 0
visited = defaultdict(int)

def find_path(cave):
    global path_count
    
    if cave == "end":
        path_count += 1
        return

    if cave.islower():
        visited[cave] += 1

        more_than_once = 0
        for c in visited:
            more_than_once += visited[c] > 1
            
            if visited[c] > 2:
                visited[cave] -= 1
                return
        
        if more_than_once > 1:
            visited[cave] -= 1
            return
    
    for n in adjacency[cave]:
        if n == "start":
            continue
        find_path(n)

    if cave.islower():
        visited[cave] -= 1

find_path("start")

print(path_count)
