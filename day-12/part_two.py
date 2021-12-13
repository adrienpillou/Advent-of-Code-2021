#PART TWO: https://adventofcode.com/2021/day/12
#DATE: 12/12/2021
#ANSWER: 

from collections import defaultdict

with open("input.txt") as file:
    x = file.read().strip()
data = [i.split("-") for i in x.split("\n")]

adjacency = defaultdict(list)

for a, b in data:
    adjacency[a].append(b)
    adjacency[b].append(a)


path_count = 0
visited = set()

def find_path(cave):
    global path_count
    
    if cave == "end":
        path_count += 1
        return

    if cave.islower() and cave in visited:
        return
    
    if cave.islower():
        visited.add(cave)
    
    for n in adjacency[cave]:
        if n == "start":
            continue
        find_path(n)

    if cave.islower():
        visited.remove(cave)

find_path("start")

print(path_count)
