#PART TWO: https://adventofcode.com/2021/day/8
#DATE: 08/12/2021
#ANSWER: 

from itertools import permutations

with open("input.txt", "r") as file:
    x = file.readlines()

x = [i.rstrip() for i in x]

signals = []
values = []

sum = 0

digits_map = {
    #     a  b  c  d  e  f  g
    "0": [1, 1, 1, 0, 1, 1, 1],
    "1": [0, 0, 1, 0, 0, 1, 0],
    "2": [1, 0, 1, 1, 1, 0, 1],
    "3": [1, 0, 1, 1, 0, 1, 1],
    "4": [0, 1, 1, 1, 0, 1, 0],
    "5": [1, 1, 0, 1, 0, 1, 1],
    "6": [1, 1, 0, 1, 1, 1, 1],
    "7": [1, 0, 1, 0, 0, 1, 0],
    "8": [1, 1, 1, 1, 1, 1, 1],
    "9": [1, 1, 1, 1, 0, 1, 1],
}



for i, l in enumerate(x):
    signals.append(l.split("|")[0].strip())
    values.append(l.split("|")[1].strip())

for i in range(len(signals)):
    signals[i] = signals[i].split()

for i in range(len(values)):
    values[i] = values[i].split()

for l, line in enumerate(signals):
    segments = ["a", "b", "c", "d", "e", "f", "g"]
    for combination in list(permutations(segments)):
        valid_combination = True
        for word in line:
            if (len(word) not in [2, 3, 4, 8]):
                continue
        print (valid_combination)
            
            


