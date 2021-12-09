#PART TWO: https://adventofcode.com/2021/day/8
#DATE: 08/12/2021
#ANSWER: 974512

from itertools import permutations

segments = "abcdefg"

digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg"
}

def decode(word, combination)->int:
    transposed_number = []
    for letter in word:
        pos = combination.index(letter)
        transposed_number.append(segments[pos])
    transposed_number = "".join(sorted(transposed_number))
    for k in digits.keys():
        if(digits[k] == transposed_number):
            return k
    return -1

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


valid_combinations = {}
for n, line in enumerate(signals):
    for combination in list(permutations(segments)):
        combination_is_valid = True
        for number in line:
            valid_number = False
            transposed_number = []
            
            for l in number:
                pos = combination.index(l)
                transposed_number.append(segments[pos])
            transposed_number = "".join(sorted(transposed_number))

            if(transposed_number in digits.values()):
                valid_number = True

            if not valid_number:
                combination_is_valid = False

        if combination_is_valid:
            valid_combinations[n] = combination

output_values = []
for l, line in enumerate(values):
    decoded_integer = 0
    for i, value in enumerate(line[::-1]):
        n = decode(value, valid_combinations[l])
        assert(n != -1)
        decoded_integer += n * 10**i
    output_values.append(decoded_integer)

print(sum(output_values))
                
            
        
            
            


