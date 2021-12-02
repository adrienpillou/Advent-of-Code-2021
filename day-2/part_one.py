#PART ONE: https://adventofcode.com/2021/day/2
#DATE: 02/12/2021
#ANSWER: 

class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
    
    def __repr__(self) -> str:
        return f"h = {self.horizontal}, d = {self.depth}, t = {self.depth*self.horizontal}"


with(open("input.txt", "r") as file):
    x = file.readlines()

x = [i.rstrip() for i in x]

submarine = Submarine()

for i in x:
    unit = i.split()[1]
    direction = i.split()[0]

    if(direction == "forward"):
        submarine.horizontal += int(unit)
    elif (direction == "down"):
        submarine.depth += int(unit)
    elif(direction == "up"):
        submarine.depth -= int(unit)
    

print(submarine)