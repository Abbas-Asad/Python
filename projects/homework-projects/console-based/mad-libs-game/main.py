def generate_mad_lib():
    name = input("Name: ").title()
    programming_language = input("Programming language: ").title()
    favourite_library = input("Favourite library: ").title()
    current_project = input("Current project: ").title()

    mad_lib = f"\nMy name is {name} and I am a {programming_language} developer. My favorite library is {favourite_library} and I am currently working on {current_project} project. One day, I will be the best {programming_language} developer in the world!"

    print(mad_lib)

generate_mad_lib()