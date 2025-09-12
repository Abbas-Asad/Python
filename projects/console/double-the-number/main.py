def double_the_number():
  user_input= int(input("Enter the number: "))
  while (user_input < 100):
    user_input *=2
    print(user_input, end=" ")

if __name__ == '__main__':
  double_the_number()