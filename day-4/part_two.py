#PART TWO: https://adventofcode.com/2021/day/4
#DATE: 04/12/2021
#ANSWER: 4624

import numpy as np

def detect_row(board) -> bool:
    """Check if the board has one complete row"""
    for j in range(5):
        row = board[j,:]
        if(not 0 in row):
            return True
    return False

def detect_column(board) -> bool:
    """Check if the board has one complete column"""
    for i in range(5):
        column = board[:,i]
        if(not 0 in column):
            return True
    return False

def is_board_winning(board) -> bool:
    """Check if a board is winning (at least one complete row or column)"""
    if(detect_column(board)):
        return True
    if (detect_row(board)):
        return True
    return False

def calculate_board_score(board, marked_board) -> int:
    """Calculate the board score using the remaining values"""
    buffer = board.copy()
    for j in range(board.shape[0]):
        for i in range(board.shape[1]):
            if (marked_board[j, i] == 1):
                buffer[j, i] = 0
    return buffer.sum()

def board_already_won(winning_boards, board_index) -> bool:
    """Check if a board is already in the winning boards list"""
    for l in winning_boards:
        if(l[0] == board_index):
            return True
    return False

def get_bingo_sequence():
    """Read the first line from the input file"""
    with open("input.txt","r") as file:
        sequence = file.readline()

    sequence = sequence.rstrip().split(",")
    sequence = [int(i) for i in sequence]
    return sequence

sequence = get_bingo_sequence()

with open("input.txt", "r") as file:
    x = file.readlines()

inline_grids = x[x.index("\n")::]

for i, r in enumerate(inline_grids):
    r = r.replace("\n", "")
    inline_grids[i] = r

boards = []
grid = []
for r in inline_grids:
    if(r == ""):
        boards.append(np.matrix(grid, int))
        grid = []
    else:
        row = [int(i) for i in r.split()]
        grid.append(row)

boards.remove(boards[0])
for g in boards:
    if(len(g) == 0):
        boards.remove(g)

marked_boards = []
shape = (5, 5)
for i in range(len(boards)):
    marked_boards.append(np.zeros(shape, int))

# Winning boards list ([board index, turn when win happens])
winning_boards = []

for turn, n in enumerate(sequence):
    for b in range(len(boards)):
        if(board_already_won(winning_boards, b)):
            continue
        if(n in boards[b]):
            y, x = np.where(boards[b] == n)
            if(len(y) == 0 and len(x) == 0):
                continue
            marked_boards[b][y, x] = 1

    for c, m in enumerate(marked_boards):
        if( board_already_won(winning_boards, c)):
            continue
        elif(is_board_winning(m)):
            winning_boards.append([c, turn])

# Reverse sort winning boards list using turn as a sorting key
k = lambda x:x[1]
winning_boards.sort(key=k, reverse=True)

last_winning_board = winning_boards[0]
last_winning_board_index = last_winning_board[0]
turn = last_winning_board[1]

score = calculate_board_score(
    boards[last_winning_board_index],
    marked_boards[last_winning_board_index]
)

print(score * sequence[turn])





    
        
        
        