import random
import requests
from bs4 import BeautifulSoup

while True:
    # input name of recipe 
    recipe_name = input("Enter a recipe name: ")

def get_recipe_from_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extracting ingredients and instructions from the website
        ingredients = [ingredient.get_text().strip() for ingredient in soup.select('.recipe-ingred_txt')]
        instructions = [step.get_text().strip() for step in soup.select('.recipe-directions__list--item')]
        return ingredients, instructions
    else:
        print("Failed to fetch the recipe from the website.")
        return [], []



def main():
    recipe_url = "https://www.allrecipes.com/recipe/222093/healthier-slow-cooker-beef-stew-i/"
    all_ingredients, all_instructions = get_recipe_from_website(recipe_url)



if __name__ == "__main__":
    main()

