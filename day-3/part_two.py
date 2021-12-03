#PART TWO: https://adventofcode.com/2021/day/3
#DATE: 03/12/2021
#ANSWER: 4105235

oxygen_rating = 0
scrubber_rating = 0

def bin_to_dec(word_list):
    dec = 0
    for i, b in enumerate(word_list[::-1]):
        if(b == 0):continue
        dec += 2**i
    return dec

def get_common_values(words, char_index):
    zeros_count = 0
    ones_count = 0
    for w in words:
        if(w[char_index] == "0"):
            zeros_count += 1
        else:
            ones_count += 1
    
    if(ones_count > zeros_count):
        return (1, 0)
    elif(ones_count < zeros_count):
        return (0, 1)
    else:
        return (1, 1)

with open("input.txt", "r") as file:
    x = file.readlines()

x = [i.rstrip() for i in x]

possible_oxygen_words = x.copy()
possible_scrubber_words = x.copy()

most_common_value = 0
least_common_value = 0


for i in range(len(x[0])):
    
    most_common_value, least_common_value = get_common_values(possible_oxygen_words, i)

    for w in possible_oxygen_words:
        if(most_common_value == least_common_value):
            for pw in possible_oxygen_words:
                if(pw[i] == "0"):
                    possible_oxygen_words.remove(pw)
        else:
            for pw in possible_oxygen_words:
                if(pw[i] == str(least_common_value)):
                    possible_oxygen_words.remove(pw)
    
    if(len(possible_oxygen_words) == 1):
        break

oxygen_word = [int(c) for c in possible_oxygen_words[0]]
oxygen_rating = bin_to_dec(oxygen_word)


for i in range(len(x[0])):
    
    most_common_value, least_common_value = get_common_values(possible_scrubber_words, i)

    for w in possible_scrubber_words:
        if(most_common_value == least_common_value):
            for pw in possible_scrubber_words:
                if(pw[i] == "1"):
                    possible_scrubber_words.remove(pw)
        else:
            for pw in possible_scrubber_words:
                if(pw[i] == str(most_common_value)):
                    possible_scrubber_words.remove(pw)
    
    if(len(possible_scrubber_words) == 1):
        break

scrubber_word = [int(c) for c in possible_scrubber_words[0]]
scrubber_rating = bin_to_dec(scrubber_word)

print(scrubber_rating * oxygen_rating)












    
