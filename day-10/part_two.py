#PART TWO: https://adventofcode.com/2021/day/10
#DATE: 10/12/2021
#ANSWER: 2802519786

from collections import defaultdict
from math import floor


with open("input.txt") as file:
    x = file.read().split("\n")

openings = ["(", "[", "{", "<"]
closings = [")", "]", "}", ">"]

points = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

def is_complete(line):
    complete = True
    for c in closings:
        if (c in line):
            return False
    return True

def find_corrupted_char(line):
    line_list = list(line)
    n = 0
    while(n < len(line_list)):
        if(len(line_list) <= 1):
            return ""
        if(is_complete("".join(line_list))):
            return ""
        char = line_list[n]
        if(char in closings):
            previous_char = line_list[n-1]
            if(previous_char == openings[closings.index(char)]):
                del line_list[n-1:n+1]
                n = 0
            else:
                return line_list[n]
        else:
            n += 1

def get_complement(line):
    line_list = list(line)
    n = 0
    while(n < len(line_list)):
        if(len(line_list) <= 1):
            return line_list[::-1]
        if(is_complete("".join(line_list))):
            return line_list[::-1]
        char = line_list[n]
        if(char in closings):
            previous_char = line_list[n-1]
            if(previous_char == openings[closings.index(char)]):
                del line_list[n-1:n+1]
                n = 0
            else:
                return line_list[::-1]
        else:
            n += 1

def flip(chars):
    for i, c in enumerate(chars):
        chars[i] = closings[openings.index(c)]
    return chars

def complete(line):
    counter = defaultdict()
    opens = []
    closes = []

    for c in openings:
        counter[c] = list(line).count(c)
    for c in closings:
        counter[c] = list(line).count(c)

    for c in line:
        if c in openings:
            opens.append(c)
        elif c in closings:
            closes.append(c)

    opens = opens[::-1]
    for i in range(len(opens)):
        opens[i] = closings[openings.index(opens[i])]
    
    for i, c in enumerate(closes):
        if(i < len(opens)):
            if c in opens:
                del opens[i]
    
    return opens

clean_input = []

for i, line in enumerate(x):
    char = find_corrupted_char(line)
    if char == "":
        clean_input.append(line)

scores = []
for line in clean_input:
    score = 0
    chars_to_add = get_complement(line)
    chars_to_add = flip(chars_to_add)
    for c in chars_to_add:
        score = (score * 5) + points[c]
    scores.append(score)

scores = sorted(scores)
mid = floor(len(scores)/2)
print(scores[mid])  


