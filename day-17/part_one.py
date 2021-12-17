#PART ONE: https://adventofcode.com/2021/day/17
#DATE: 17/12/2021
#ANSWER: 4095

# x=244..303, y=-91..-54
target_area = [[244, 303], [-91, -54]]

probe_initial_velocity = (6, 9)
probe_position = [0, 0]
probe_velocity = [0, 0]

def move_probe():
    probe_position[0] += probe_velocity[0]
    probe_position[1] += probe_velocity[1]

    if(probe_velocity[0] > 0):
        probe_velocity[0] -= 1
    elif(probe_velocity[0] < 0):
        probe_velocity[0] += 1

    probe_velocity[1] -= 1

def main():
    global probe_velocity
    probe_velocity = list(probe_initial_velocity)
    in_area = False
    safety = 2**8
    s = 0
    probe_history = []
    while(not in_area):
        move_probe()
        probe_history.append(probe_position.copy())
        if(within_area()):
            in_area = True
        s+=1
        if(s>safety):
            break
    
    if(in_area):
        probe_history.sort(key=lambda x:x[1], reverse=True)
        return probe_history[0][1]
    else:
        
        return -1

def  within_area():
    x, y = probe_position
    target_x = target_area[0][0]
    target_y = target_area[1][0]
    target_w = abs(target_area[0][1] - target_area[0][0])
    target_h = abs(target_area[1][1] - target_area[1][0])
    
    if x >= target_x and x <=target_x + target_w:
        if y >= target_y and y <= target_y + target_h:
            return True
    return False

max_height = 0
for x in range(100):
    for y in range(100):
        probe_initial_velocity = (x, y)
        probe_position = [0, 0]
        height = main()
        if(height > max_height):
            max_height = height
            print(max_height, "Initial velocity: ", probe_initial_velocity)
        