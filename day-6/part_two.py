#PART TWO: https://adventofcode.com/2021/day/6
#DATE: 06/12/2021
#ANSWER: 1650309278600

with open("input.txt", "r") as file:
    x = file.readline()
x = [int(i) for i in x.split(",")]

limit = 256

fishes = {}
for v in range(9):
    fishes[v] = 0

for i in x:
    fishes[i] += 1

for d in range(limit):
    new_fishes = {}
    for v in range(9):
        new_fishes[v] = 0
    
    for (f, count) in fishes.items():
        if(f == 0):
            new_fishes[6] += count
            new_fishes[8] += count
        else:
            new_fishes[f-1] += count
    fishes = new_fishes

print(sum(fishes.values()))

