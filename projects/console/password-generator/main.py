import random

def generate_password():
    print("Welcome to your Password Generator!")

    chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*-_+"

    number = int(input('Amount of passwords to generate: '))
    length = int(input('Input your password length: '))

    for _ in range(number):
        password = ''.join(random.choice(chars) for _ in range(length))
        print(password)

generate_password()