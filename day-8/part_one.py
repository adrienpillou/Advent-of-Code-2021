#PART ONE: https://adventofcode.com/2021/day/8
#DATE: 08/12/2021
#ANSWER: 367

with open("input.txt", "r") as file:
    x = file.readlines()

x = [i.rstrip() for i in x]

signals = []
values = []

for i, l in enumerate(x):
    signals.append(l.split("|")[0].strip())
    values.append(l.split("|")[1].strip())

for i in range(len(signals)):
    signals[i] = signals[i].split()

for i in range(len(values)):
    values[i] = values[i].split()

digits = [2, 4, 3, 7]

count = 0
for line in values:
    for value in line:
        if(len(value) in digits):
            count += 1
        
print(count)