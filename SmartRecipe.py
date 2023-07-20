import random
import os

def read_recipe(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.readlines()
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []

def generate_recipe(title, ingredients, instructions):
    recipe = f"\n{title}\n\nIngredients:\n"
    random.shuffle(ingredients)
    for ingredient in ingredients:
        recipe += f"- {ingredient.strip()}\n"

    recipe += "\nInstructions:\n"
    random.shuffle(instructions)
    for idx, instruction in enumerate(instructions, start=1):
        recipe += f"{idx}. {instruction.strip()}\n"

    return recipe

def main():
    recipe_files = [
        "Users/kingcharles/banana bread.txt",
        "Users/kingcharles/black bean chili.txt",
        "Users/kingcharles/Pasta Salad.txt",
    ]

    # Modify the file paths to be absolute paths using os.path.abspath()
    home_directory = os.path.expanduser("~")
    recipe_files = [os.path.abspath(os.path.join(home_directory, file_path)) for file_path in recipe_files]

    all_ingredients = []
    all_instructions = []

    for file_path in recipe_files:
        ingredients, instructions = read_recipe(file_path)

        # Debugging statements
        print(f"File: {file_path}")
        print("Ingredients:", ingredients)
        print("Instructions:", instructions)

        all_ingredients.extend(ingredients)
        all_instructions.extend(instructions)

    while True:
        print("Menu:")
        print("1. Generate Smart Recipe")
        print("2. Quit")

        choice = input("Enter your choice (1/2): ")

        if choice == '1':
            title = "Smart Recipe"
            random_recipe = generate_recipe(title, all_ingredients, all_instructions)
            print(random_recipe)
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()


