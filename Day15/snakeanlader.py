import random

def dice():
    return random.randint(1, 6)

def get_valid_input(player):
    while True:
        status = input(f"[Player {player}] [P]lay or [Q]uit: ").lower()
        if status in ['p', 'q']:
            return status
        else:
            print("Invalid input! Enter P or Q")

def move_player(score, dice_val):
    
    if score + dice_val > 100:
        print("Cannot move! Need exact number to reach 100")
        return score
    
    score += dice_val

    if score in ladders:
        print(f"Ladder! Jump to {ladders[score]}")
        score = ladders[score]

    elif score in snakes:
        print(f"Snake! Down to {snakes[score]}")
        score = snakes[score]

    return score


player1_score = 0
player2_score = 0

ladders = {6:25, 12:31, 35:90, 46:60, 51:74, 78:99, 82:96}
snakes = {24:5, 45:18, 66:33, 74:37, 88:77, 93:57, 98:21}

turn = 1

while player1_score < 100 and player2_score < 100:

    if turn == 1:

        status = get_valid_input(1)
        if status == 'q':
            print("Player 1 Quit!")
            break

        dice_val = dice()
        print(f"Dice: {dice_val}")

        player1_score = move_player(player1_score, dice_val)

        print(f"Player 1 Score: {player1_score}\n")

        turn = 2

    else:

        status = get_valid_input(2)
        if status == 'q':
            print("Player 2 Quit!")
            break

        dice_val = dice()
        print(f"Dice: {dice_val}")

        player2_score = move_player(player2_score, dice_val)

        print(f"Player 2 Score: {player2_score}\n")

        turn = 1


if player1_score == 100:
    print("Player 1 Wins!")

elif player2_score == 100:
    print("Player 2 Wins!")

else:
    print("Game Ended Early.")