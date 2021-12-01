#PART TWO: https://adventofcode.com/2021/day/1
#DATE: 01/12/2021
#ANSWER: 1797

delta = 0
increased_count = 0
measurements = []
cleaned_measurements = []

with open("./input.txt", "r") as file:
    x = file.readlines()

measurements = [int(i) for i in x]

for i, m in enumerate(measurements):
    if(i>len(measurements)-3):continue
    cleaned_measurements.append(measurements[i] + measurements[i+1] + measurements[i+2])

for i in range(1, len(cleaned_measurements)):
    if(i<1):continue
    delta = cleaned_measurements[i] - cleaned_measurements[i-1]
    if(delta>0):
        increased_count += 1
        
print(increased_count)