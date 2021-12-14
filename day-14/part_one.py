#PART ONE: https://adventofcode.com/2021/day/14
#DATE: 14/12/2021
#ANSWER: 3143

with open("input.txt")as file:
    x = file.read().split("\n")

template = x[0]
sections = x[2:]

for i, s in enumerate(sections):
    sections[i] = sections[i].split(" -> ")
    sections[i] = tuple(sections[i])

def insert(template):
    buffer = ""
    i = 0
    while i < len(template)-1:
        pair = template[i:i+2]
        buffer += pair[0]
        for section in sections:
            char = section[1]
            if section[0] == pair:
                buffer += char 
                break
        i += 1
    buffer += pair[-1]
    return buffer
        
steps = 10
print(f"Template: {template}")
for i in range(steps):
    template = insert(template)

char_set = "".join(set(template))

char_dict = {}
for c in char_set:
    char_dict[c] = template.count(c)

ocurrences = sorted(char_dict.values(), reverse=True)
print(ocurrences[0] - ocurrences[-1])