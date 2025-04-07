import random

random_number = random.randint(0, 99)

def guess_the_number():
    number_of_guesses = 0
    while True:
        number_of_guesses += 1
        if  number_of_guesses < 11:
            user_input  = int(input("Guess the number from 0 to 99: "))
            if user_input < random_number:
                print("Your guess is too low")

            elif user_input > random_number:
                print("Your guess is too high")
            
            else:
                print(f"\nCongrats! The number was {random_number} and you guessed it correctly🎉 \nYour marks are {11 - number_of_guesses}/10")
                break

        else: 
            print("\nYou lose!")
            break
            
guess_the_number()
