#PART ONE: https://adventofcode.com/2021/day/3
#DATE: 03/12/2021
#ANSWER: 3847100

power_consumption = 0
gamma_rate_position = []
epsilon_rate_position = []
gamma_rate = 0
epsilon_rate = 0

def bin_to_dec(word_list):
    dec = 0
    for i, b in enumerate(word_list[::-1]):
        if(b == 0):continue
        dec += 2**i
    return dec

with open("input.txt", "r") as file:
    x = file.readlines()

x = [i.rstrip() for i in x]

for i in range(len(x[0])):
    zeros_count = 0 
    for w in x:
        if w[i] == "0":
            zeros_count += 1
    if(zeros_count > len(x)-zeros_count):
        epsilon_rate_position.append(i)
    else:
        gamma_rate_position.append(i)

gamma_word = [0] * len(x[0])
epsilon_word = [0] * len(x[0])

for i in range(12):
    if(i in gamma_rate_position):
        gamma_word[i] = 1
    else:
        gamma_word[i] = 0

for i in range(12):
    if(i in epsilon_rate_position):
        epsilon_word[i] = 1
    else:
        epsilon_word[i] = 0

gamma_rate = bin_to_dec(gamma_word)
epsilon_rate = bin_to_dec(epsilon_word)

print("g: ",gamma_word, gamma_rate)
print("e: ", epsilon_word, epsilon_rate)

print(gamma_rate*epsilon_rate)