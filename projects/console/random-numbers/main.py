import random

def generate_ten_random_numbers():
  for _ in range(1, 11):
    random_number = random.randint(1, 100)
    print(random_number, end=" ")

if __name__ == '__main__':
  generate_ten_random_numbers()