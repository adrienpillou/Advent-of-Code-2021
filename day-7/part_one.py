#PART ONE: https://adventofcode.com/2021/day/7
#DATE: 07/12/2021
#ANSWER: 347011

with open("input.txt", "r") as file:
    x = file.readline()
x = [int(i) for i in x.split(",")]

scenarios = []
for i, position in enumerate(range(min(x), max(x)+1)):
    target_position = position
    fuel = 0
    for crab_position in x:
        if(target_position != crab_position):
            steps = abs(target_position - crab_position)
            fuel += steps
    scenarios.append(fuel)

print(min(scenarios))