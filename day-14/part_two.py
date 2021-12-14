#PART TWO: https://adventofcode.com/2021/day/14
#DATE: 14/12/2021
#ANSWER: 4110215602456

from collections import defaultdict
from copy import copy

with open("input.txt")as file:
    x = file.read().split("\n")

template = x[0]
sections = x[2:]

for i, s in enumerate(sections):
    sections[i] = sections[i].split(" -> ")
    sections[i] = tuple(sections[i])

frequencies = defaultdict(int)

def load_polymer(template):
    pairs = defaultdict(int)
    for i in range(len(template)-1):
        pair = template[i:i+2]
        pairs[pair] += 1
    return pairs

def insert():
    global frequencies
    new_frequencies = copy(frequencies)
    for f in frequencies:
        for pair, char in sections:
            if f == pair:
                occurrences = frequencies[pair]
                new_frequencies[pair] -= occurrences
                new_frequencies[pair[0] + char] += occurrences
                new_frequencies[char + pair[1]] += occurrences
                break
    return new_frequencies

steps = 40
print(f"Template: {template}")

frequencies = load_polymer(template)
for i in range(steps):
    frequencies = insert()
    print(f"Step {i+1}...")

char_dict = defaultdict(int)

for key in frequencies.keys():
    for c in key:
        char_dict[c] += frequencies[key]

for key in char_dict.keys():
    char_dict[key] = char_dict[key] // 2

char_dict[template[0]] += 1
char_dict[template[-1]] += 1

counts = sorted(char_dict.values(), reverse=True)
print(counts[0] - counts[-1])