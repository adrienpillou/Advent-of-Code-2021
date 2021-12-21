
class Player():
    def __init__(self, id, position) -> None:
        self.id = id
        self.position = position
        self.score = 0

track = [i+1 for i in range(10)]

turn = 0
die = 1

p1 = Player(1, 4)
p2 = Player(2, 10)

players = [p1, p2]


def play_turn(player, rolls):
    player.position += sum(rolls)
    player.position = player.position % 10
    if player.position == 0:
        player.position = 10
    player.score += player.position
    print(f"Player {player.id} rolls {rolls[0]} + {rolls[1]} + {rolls[2]} and moves to space {player.position} for a total score of {player.score}")

while p1.score < 1000 and p2.score < 1000:
    rolls = [die, die + 1, die + 2]
    if turn % 2 == 0:
        play_turn(p1, rolls)
    elif turn % 2 == 1:
        play_turn(p2, rolls)
    die += 3
    turn += 1

total_rolls = turn*3 
if(p1.score > p2.score):
    print("Player 1 wins")
    print(p2.score * total_rolls)
else: 
    print("Player 2 wins")
    print(p1.score * total_rolls)



