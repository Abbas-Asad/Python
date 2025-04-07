a_to_z_words = [
    "Apple",
    "Ball",
    "Cat",
    "Dog",
    "Elephant",
    "Fish",
    "Goat",
    "Hat",
    "Ice cream",
    "Juice",
    "Kite",
    "Lion",
    "Monkey",
    "Nest",
    "Orange",
    "Parrot",
    "Queen",
    "Rabbit",
    "Sun",
    "Tiger",
    "Umbrella",
    "Van",
    "Watch",
    "Xylophone",
    "Yoyo",
    "Zebra"
]

def a_to_z_word_finder():
    print("🔤 Welcome to A to Z Word Finder for Kids!\n")
    letter = input("Please enter an alphabet letter (A-Z): ").strip().upper()

    for word in a_to_z_words:
        if letter == word[0]:
            print(f"{word[0]} for {word}.")
            break

a_to_z_word_finder()