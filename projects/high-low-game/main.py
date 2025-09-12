import random

def play_high_low_game():
  print("""Welcome to the High-Low Game!
-----------------------------""")
  score = 0

  for i in range(1,6):
    computer_random_number = random.randint(1, 100)
    user_random_number = random.randint(1, 100)

    if computer_random_number > user_random_number:
      correct_answer = "lower"

    elif computer_random_number < user_random_number:
      correct_answer = "higher"

    print(f"\nRound {i}")
    print(f"Your number is {user_random_number}")
    user_input = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()

    if user_input == correct_answer:
      score += 1
      print(f"You were right! The computer's number was {computer_random_number}")
      print(f"Your score is now {score}")

    else:
      print(f"Aww, that's incorrect. The computer's number was {computer_random_number}")
      print(f"Your score is now {score}")

  print("\nThanks for playing!")

if __name__ == "__main__":
  play_high_low_game()