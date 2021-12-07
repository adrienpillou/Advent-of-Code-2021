#PART TWO: https://adventofcode.com/2021/day/7
#DATE: 07/12/2021
#ANSWER: 98363777

cache = {}

with open("input.txt", "r") as file:
    x = file.readline()
x = [int(i) for i in x.split(",")]

def calculate_cost(steps):
    if(steps in cache.keys()):
        return cache[steps]
    cost = 0
    for s in range(1, steps+1):
        cost += s
    cache[steps] = cost
    return cost

scenarios = []
for i, position in enumerate(range(min(x), max(x)+1)):
    target_position = position
    fuel = 0
    for crab_position in x:
        if(target_position != crab_position):
            steps = abs(target_position - crab_position)
            fuel += calculate_cost(steps)
    scenarios.append(fuel)

print(min(scenarios))

