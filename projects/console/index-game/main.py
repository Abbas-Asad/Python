# Problem 1: List Practice
fruit_list : list = [ 'apple', 'banana', 'orange', 'grape', 'pineapple' ]
print(f"Length of fruit list is: {len(fruit_list)}")
fruit_list.append("mango")
print(f"Updated fruit list is: {fruit_list}")

# Problem 2: Index Game
def access_elements(lst, index):
  try:
    value = lst[index]
    return value
  except IndexError:
    return "Out of range!"

def modify_elements(list_to_modify, index, new_value):
  try:
    list_to_modify[index] = new_value
    return list_to_modify

  except IndexError:
    return "Out of range!"

def slice_the_list(list_to_slice, start_index, end_index):
  try:
    return list_to_slice[start_index : end_index]

  except IndexError:
    return "Out of range!"

def play_index_game():
    lst = [1, 2, 3, 4, 5]
    print(f"Our Current list is: {lst}")

    operation = input("Choose an operation: access, modify, slice: ").strip().lower()

    if operation == "access":
      index = int(input("Enter index to access: "))
      print(access_elements(lst, index))

    elif operation == "modify":
      index = int(input("Enter index to modify: "))
      new_value = input("Enter new value: ")
      print(modify_elements(lst, index, new_value))

    elif operation == "slice":
      start_index = int(input("Enter start index: "))
      end_index = int(input("Enter end index: "))
      print(slice_the_list(lst, start_index, end_index))

    else:
        print("Invalid operation.")

if __name__ == "__main__":
  play_index_game()