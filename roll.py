
import random
def roll_dice():
    return random.randint(1,6)
player_score = 0
computer_score = 0
for i in range(5):
    print("\nRound", i+1)
    player = roll_dice()
    computer = roll_dice()
    print("Player rolled:", player)
    print("Computer rolled:", computer)
    if player > computer:
        player_score += 1
        print("Player wins this round")
    elif computer > player:
        computer_score += 1
        print("Computer wins this round")
    else:
        print("Draw")
        print("\nFinal Score")
        print("Player:", player_score)
        print("Computer:", computer_score)
    if player_score > computer_score:
        print("Player Wins Game")
    elif computer_score > player_score:
        print("Computer Wins Game")
    else:
        print("Game Draw")
