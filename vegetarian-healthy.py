import requests
import re
from bs4 import BeautifulSoup
import nltk
from nltk.tokenize import sent_tokenize

from difflib import get_close_matches

# Recipe retrieval and display
def get_recipe_details(url):
    try:
        # Attempt to fetch the URL
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx, 5xx)
    except requests.exceptions.MissingSchema:
        print("Invalid URL format.")
        return
    except requests.exceptions.ConnectionError:
        print("Failed to establish a connection.")
        return
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return
    except Exception as err:
        print(f"An error occurred: {err}")
        return

        
    html_data = response.text
    soup = BeautifulSoup(html_data, "html.parser")
    title = soup.title.text

    ingredient_list = soup.find_all(class_="mm-recipes-structured-ingredients__list")
    ingredients = []
    for _ in ingredient_list:
        for __ in _:
            if __.text != "" and __.text.isspace() == False:
                ingredients.append(__.text.strip()) 

    step_list = soup.select('.comp.mntl-sc-block.mntl-sc-block-startgroup.mntl-sc-block-group--LI .comp.mntl-sc-block.mntl-sc-block-html')
    steps = []  
    for i in range(len(step_list)):
        sentences = sent_tokenize(step_list[i].text.strip())
        steps.extend(sentences)
    
    return title, ingredients, steps

def show_ingredients(ingredients):
    print("Here are the ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")

def replace_meat_with_vegetarian(ingredients):
    # Define common meat-related keywords and their vegetarian alternatives
    meat_to_veg = {
        "chicken": "tofu",
        "beef": "tempeh",
        "pork": "jackfruit",
        "sausage": "vegan sausage",
        "bacon": "vegan bacon",
        "turkey": "seitan",
        "ham": "smoked tofu",
        "ground beef": "plant-based ground meat",
        "meatballs": "vegetarian meatballs",
        "hot dog": "veggie dog"
    }
    
    updated_ingredients = []
    for ingredient in ingredients:
        lower_ingredient = ingredient.lower()
        replacement_found = False
        
        # Check for meat keywords in the ingredient and replace if found
        for meat, vegetarian in meat_to_veg.items():
            if meat in lower_ingredient:
                updated_ingredients.append(ingredient.replace(meat, vegetarian, 1))
                replacement_found = True
                break
        
        # If no replacement found, keep the ingredient as is
        if not replacement_found:
            updated_ingredients.append(ingredient)
    
    return updated_ingredients


def replace_with_healthy_alternatives(ingredients):
    # Define common unhealthy ingredients and their healthier substitutes
    unhealthy_to_healthy = {
        "sugar": "honey",
        "white flour": "whole wheat flour",
        "butter": "olive oil",
        "cream": "coconut cream",
        "whole milk": "2% milk",
        "bacon": "turkey bacon",
        "mayonnaise": "Greek yogurt",
        "salt": "reduced-sodium salt",
        "fried": "baked",
        "white rice": "brown rice or quinoa",
        "potato chips": "sweet potato chips",
        "lard": "avocado oil",
        "pasta": "whole wheat pasta",
        "candy": "dried fruits",
        "deep-fried": "baked",
        "ketchup": "tomato paste and spices"
    }

    updated_ingredients = []
    for ingredient in ingredients:
        lower_ingredient = ingredient.lower()
        replacement_found = False

        # Check for unhealthy keywords in the ingredient and replace if found
        for unhealthy, healthy in unhealthy_to_healthy.items():
            if unhealthy in lower_ingredient:
                updated_ingredients.append(ingredient.replace(unhealthy, healthy, 1))
                replacement_found = True
                break

        # If no replacement found, keep the ingredient as is
        if not replacement_found:
            updated_ingredients.append(ingredient)

    return updated_ingredients

# Main
# url = input()
url = "https://www.allrecipes.com/recipe/49404/juiciest-hamburgers-ever/"
# https://www.allrecipes.com/butternut-squash-chili-recipe-8725719

title, ingredients, steps = get_recipe_details(url)

show_ingredients(ingredients)

veg_ingredients = replace_meat_with_vegetarian(ingredients)
show_ingredients(veg_ingredients)

healthy_ingredients = replace_with_healthy_alternatives(ingredients)
show_ingredients(healthy_ingredients)



