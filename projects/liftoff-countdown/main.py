import time

def countdown():
  for i in range(10,0,-1):
    print(f"{i}...")
    time.sleep(1)

  print("Liftoff!")

if __name__ == '__main__':
  countdown()