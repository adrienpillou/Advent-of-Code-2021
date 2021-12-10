#PART ONE: https://adventofcode.com/2021/day/10
#DATE: 10/12/2021
#ANSWER: 168417

with open("input.txt") as file:
    x = file.read().split("\n")

openings = ["(", "[", "{", "<"]
closings = [")", "]", "}", ">"]

points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
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
                #print("".join(line_list))
                n = 0
            else:
                return line_list[n]
        else:
            n += 1

sum = 0
for i, line in enumerate(x):
    char = find_corrupted_char(line)
    if char != "":
        sum += points[char]

print(sum)


    