#PART ONE: https://adventofcode.com/2021/day/6
#DATE: 06/12/2021
#ANSWER: 365131

class Fish:
    def __init__(self, timer):
        self.internal_timer = timer
    
    def __repr__(self):
        return f"[{self.internal_timer}]"

with open("input.txt", "r") as file:
    x = file.readline()

fishes = []
new_fishes = []
limit = 80

x = [int(i) for i in x.split(",")]

for i in x:
    fish = Fish(i)
    fishes.append(fish)

for d in range(80):
    new_fishes = []
    for f in fishes:
        f.internal_timer -= 1
        if(f.internal_timer < 0):
            f.internal_timer = 6
            new_fishes.append(Fish(8))
    for n in new_fishes:
        fishes.append(n)

print(len(fishes))

