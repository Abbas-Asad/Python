import random

computer = random.choice(['r', 'p', 's'])
user_input = input("Select one: r, p, s ")

def play_rps():
    if user_input == computer:
        print("Tie!")

    elif (user_input=='r' and computer =='s') or (user_input=='s' and computer =='p') or (user_input == 'p' and computer == 'r'):
        print("You won!")

    else:
        print("You lose!")

play_rps()