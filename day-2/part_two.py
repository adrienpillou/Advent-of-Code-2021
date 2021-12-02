#PART TWO: https://adventofcode.com/2021/day/2
#DATE: 02/12/2021
#ANSWER: 1845455714

class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0
    
    def __repr__(self) -> str:
        return f"h = {self.horizontal}, d = {self.depth}, t = {self.depth*self.horizontal}"


with(open("input.txt", "r") as file):
    x = file.readlines()

x = [i.rstrip() for i in x]

submarine = Submarine()

for i in x:
    direction = i.split()[0]
    unit = int(i.split()[1])

    if(direction == "forward"):
        submarine.horizontal += unit
        submarine.depth += submarine.aim * unit
    elif (direction == "down"):
        submarine.aim += unit
    elif(direction == "up"):
        submarine.aim -= unit
    

print(submarine)