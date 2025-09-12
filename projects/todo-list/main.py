todos = []
print("Welcome to iTasks!\n")
while True:
    user_input = input("Add a task: ")
    todos.append(user_input)
    want_to_add_more = input("Want to add more? y or n ")
    if want_to_add_more == "n":
        print("\nHere are your todos: ")
        for todo in todos:
            print(f"- {todo.title()}")
        break