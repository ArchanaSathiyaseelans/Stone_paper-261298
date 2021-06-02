import random

def play():
    user = input(" Choose a option  'r' for rock, 'p' for paper, 's' for scissors : " )
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "It's a tie"

    if is_win(user, computer):
        return "You won"

    return "you Lost!"


def is_win(Player, opponent):
    #return true if player wins
    # r > s, s > p, p > r
    if (Player == 'r' and opponent == 's') or (Player == 's' and opponent == 'p') or (Player == 'p' and opponent == 'r'):
        return True

print(play())