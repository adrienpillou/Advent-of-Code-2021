#PART TWO: https://adventofcode.com/2021/day/17
#DATE: 17/12/2021
#ANSWER: 3773

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

    while(not in_area):
        move_probe()
        if(within_area()):
            in_area = True
        if(probe_position[1] < target_area[1][0]):
            break
    if(in_area):
        return True
    else:
        return False

def get_area_width():
    return abs(target_area[0][1] - target_area[0][0])

def get_area_height():
    return abs(target_area[1][1] - target_area[1][0])

def within_area():
    x, y = probe_position
    target_x1 = target_area[0][0]
    target_x2 = target_area[0][1]
    target_y1 = target_area[1][0]
    target_y2 = target_area[1][1]

    if(x >= target_x1 and x <= target_x2):
        if(y >= target_y1 and y <= target_y2):
            return True
    return False

valid_velocities_count = 0
max_vertical_velocity = -target_area[1][0]
min_vertical_velocity = target_area[1][0]
for x in range(-400, 400):
    for y in range(min_vertical_velocity, max_vertical_velocity):
        probe_initial_velocity = (x, y)
        probe_position = [0, 0]
        if (main()):
            valid_velocities_count += 1

print(valid_velocities_count)

       