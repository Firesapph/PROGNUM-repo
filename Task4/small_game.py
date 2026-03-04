import numpy as np
print("Welcome to Rock-Paper-Scissors \nType 'R' for Rock, 'P' for Paper or 'S' for Scissors")

def play_game():
    '''Determines the winner based on the user choice and computer choice'''
    choices = ['R', 'P', 'S']
    user_choice = input('R, P or S: ')
    computer_choice = np.random.choice(choices)
    print(f"You: {user_choice} against computer: {computer_choice}")
    if user_choice==computer_choice:
        return 'No winner'
    elif choices.index(user_choice) == (choices.index(computer_choice) - 1):
        return 'Computer won'
    else:
        return 'You won :)'

print(play_game())