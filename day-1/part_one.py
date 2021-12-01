#PART ONE: https://adventofcode.com/2021/day/1
#DATE: 01/12/2021
#ANSWER: 1766

delta = 0
increased_count = 0
measurements = list

with open("./input.txt", "r") as file:
    x = file.readlines()

measurements = [int(i) for i in x]

print(len(x))
for i in range(1, len(x)):
    if(i<1):continue
    delta = measurements[i] - measurements[i-1]
    if(delta>0):
        increased_count += 1

print(increased_count)