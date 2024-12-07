import requests
import re
from bs4 import BeautifulSoup
from nltk.tokenize import sent_tokenize

# parsing
def get_recipe_details(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as err:
        print(f"An error occurred: {err}")
        return None

    html_data = response.text
    soup = BeautifulSoup(html_data, "html.parser")
    title = soup.title.text.strip()

    ingredient_list = soup.find_all(class_="mm-recipes-structured-ingredients__list")
    ingredients = []
    for group in ingredient_list:
        for item in group:
            if item.text.strip() and not item.text.isspace():
                ingredients.append(item.text.strip())

    step_list = soup.select('.comp.mntl-sc-block.mntl-sc-block-startgroup.mntl-sc-block-group--LI .comp.mntl-sc-block.mntl-sc-block-html')
    steps = []
    for step in step_list:
        sentences = sent_tokenize(step.text.strip())
        steps.extend(sentences)

    return title, ingredients, steps


def transform_to_italian(ingredients, steps):
    ingredient_map = {
        "onion powder" : "chopped onions",
        "ground pork" : "italian sausage",
        "noodles" : "spaghetti",
        "vinegar" : "cooking wine",
        "vegetable oil": "extra virgin olive oil",
        "ground beef": "italian sausage",
        "cheddar cheese": "parmesan cheese",
        "bread": "focaccia",
        "tomato paste": "fresh tomatoes",
        "cream": "mascarpone",
        "mushrooms": "porcini mushrooms",
        "dried herbs": "fresh basil",
        "onion": "shallots",
        "garlic powder": "fresh garlic",
        "sour cream" : "ricotta cheese",
        "bell peppers" : "sundried tomatoes", 
        "spinach" : "argula",
        "parsley" : "fresh basil",
        "bay leaf" : "rosemary"
    }

    transformed_ingredients = []
    for ingredient in ingredients:
        for old, new in ingredient_map.items():
            if old in ingredient.lower():
                ingredient = ingredient.lower().replace(old, new)
        transformed_ingredients.append(ingredient)

    transformed_steps = []
    for step in steps:
        for old, new in ingredient_map.items():
            step = step.replace(old, new)
        transformed_steps.append(step)

    return transformed_ingredients, transformed_steps


def transform_to_mexican(ingredients, steps):
    ingredient_map = {
        
        "ground pork" : "chorizo",
        "cheddar cheese": "queso fresco",
        "mozarella cheese" : "queso fresco",
        "parmesan cheese" : "queso fresco",
        "ground beef": "chorizo",
        "bread": "corn tortillas",
        "vegetable oil": "lard",
        "sour cream" : "crema",
        "cream": "crema",
        "tomatoes": "tomatillos",
        "beans": "black beans",
        "rice": "mexican rice",
        "chili powder": "chipotle powder",
        "lettuce": "shredded cabbage",
        "parsley" : "cilantro",
        "lemon" : "lime",
        "vinegar" : "lime juice",
        "chickpeas" : "black beans",
        "ketchup" : "tomato sauce",
        "bell pepper" : "jalapeno",
        "scallions" : "cilantro"
    }

    transformed_ingredients = []
    for ingredient in ingredients:
        for old, new in ingredient_map.items():
            if old in ingredient.lower():
                ingredient = ingredient.lower().replace(old, new)
        transformed_ingredients.append(ingredient)

    transformed_steps = []
    for step in steps:
        for old, new in ingredient_map.items():
            step = step.replace(old, new)
        transformed_steps.append(step)

    return transformed_ingredients, transformed_steps


def transform_to_gluten_free(ingredients, steps):
    gluten_free_substitutes = {
        "flour": "gluten-free all-purpose flour",
        "wheat flour": "gluten-free all-purpose flour",
        "breadcrumbs": "gluten-free breadcrumbs",
        "pasta": "gluten-free pasta",
        "lasagna noodles": "gluten-free lasagna noodles",
        "soy sauce": "gluten-free tamari",
        "barley": "quinoa",
        "rye": "millet",
        "couscous": "cauliflower rice",
        "crackers": "gluten-free crackers",
        "milk": "lactose-free milk",
        "butter": "lactose-free butter",
        "cream": "lactose-free cream",
        "cheese": "lactose-free cheese",
        "yogurt": "lactose-free yogurt",
    }

    transformed_ingredients = []
    for ingredient in ingredients:
        for original, substitute in gluten_free_substitutes.items():
            ingredient = ingredient.replace(original, substitute)
        transformed_ingredients.append(ingredient)

    transformed_steps = []
    for step in steps:
        for original, substitute in gluten_free_substitutes.items():
            step = step.replace(original, substitute)
        transformed_steps.append(step)

    # print("Original Ingredients:", ingredients)
    # print("Gluten-Free Ingredients:", transformed_ingredients)
    # print("\nOriginal Steps:")
    # print("\n".join(steps))
    # print("\nGluten-Free Steps:")
    # print("\n".join(transformed_steps))
    
    return transformed_ingredients, transformed_steps


def transform_to_lactose_free(ingredients, steps):
    lactose_free_substitutes = {
        "milk": "lactose-free milk",
        "butter": "lactose-free butter",
        "cream": "lactose-free cream",
        "cheese": "lactose-free cheese",
        "parmesan cheese": "lactose-free Parmesan cheese",
        "mozzarella cheese": "lactose-free mozzarella cheese",
        "yogurt": "lactose-free yogurt",
        "cottage cheese": "lactose-free cottage cheese",
        "sour cream": "lactose-free sour cream",
        "evaporated milk": "lactose-free evaporated milk",
        "condensed milk": "lactose-free condensed milk",
    }

    transformed_ingredients = []
    for ingredient in ingredients:
        for original, substitute in lactose_free_substitutes.items():
            ingredient = ingredient.replace(original, substitute)
        transformed_ingredients.append(ingredient)

    transformed_steps = []
    for step in steps:
        for original, substitute in lactose_free_substitutes.items():
            step = step.replace(original, substitute)
        transformed_steps.append(step)
    
    return transformed_ingredients, transformed_steps


def save_recipe_to_file(filename, title, ingredients, steps):
    with open(filename, "w") as f:
        f.write(f"{title}\n\nIngredients:\n")
        for ingredient in ingredients:
            f.write(f"- {ingredient}\n")
        f.write("\nSteps:\n")
        for i, step in enumerate(steps, 1):
            f.write(f"{i}. {step}\n")


def main():
    print("Welcome to the Recipe Transformer!")
    url = input("Enter the URL of a recipe from AllRecipes: ").strip()
    recipe_details = get_recipe_details(url)

    if not recipe_details:
        print("Failed to fetch recipe. Please try again.")
        return

    title, ingredients, steps = recipe_details
    print(f"\nSuccessfully fetched recipe: {title}\n")

    print("What cuisine would you like to transform this recipe into?")
    print("[1] Italian")
    print("[2] Mexican")
    print("[3] Gluten-free")
    print("[4] Lactose-free")
    cuisine_choice = input("Enter the corresponding number: ").strip()

    if cuisine_choice == "1":
        new_ingredients, new_steps = transform_to_italian(ingredients, steps)
        cuisine = "Italian"
    elif cuisine_choice == "2":
        new_ingredients, new_steps = transform_to_mexican(ingredients, steps)
        cuisine = "Mexican"
    elif cuisine_choice == "3":
        new_ingredients, new_steps = transform_to_gluten_free(ingredients, steps)
    elif cuisine_choice == "3":
        new_ingredients, new_steps = transform_to_lactose_free(ingredients, steps)
    else:
        print("Invalid choice. Exiting.")
        return

    output_filename = f"{title.replace(' ', '_')}_{cuisine}_Recipe.txt"
    save_recipe_to_file(output_filename, f"{title} - {cuisine} Style", new_ingredients, new_steps)
    print(f"\nTransformed recipe saved to {output_filename}")

if __name__ == "__main__":
    main()
