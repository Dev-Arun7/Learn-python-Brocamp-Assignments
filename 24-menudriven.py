pantry = {
     "chicken": 5,
    "pizza":1,
    "egg":4,
    "butter":4,
    "bread":7,
    "bean":2,
    "potatoes":3,
    "salt":30,
    "malt vinegar":50
    
}

recipes = {
     "Chicken and chips": [
        "chicken",
        "potatoes",
        "salt",
        "malt vinegar",
    ],
    "Pizza": [
        "pizza",
    ],
    "Egg sandwich": [
        "egg",
        "bread",
        "butter",
    ],
    "Beans on toast": [
        "beans",
        "bread",
    ]
}

def cook_recipe(recipe_name):
    recipe_ingredients = recipes.get(recipe_name)
    if recipe_ingredients is None:
        print("Recipe not found.")
        return
    
    for ingredient in recipe_ingredients:
        if ingredient in pantry:
            if pantry[ingredient] > 0:
                pantry[ingredient] -= 1
            else:
                print(f"Insufficient {ingredient} in pantry.")
                return
        else:
            print(f"{ingredient} not found in pantry.")
            return
    
    print(f"{recipe_name} cooked successfully.")
    
def display_pantry():
    print("\nCurrent Pantry:")
    for ingredient, quantity in pantry.items():
        print(f"{ingredient}: {quantity}")
    print()

def display_recipes():
    print("\nAvailable Recipes:")
    for recipe_name in recipes.keys():
        print(recipe_name)
    print()

while True:
    print("Menu:")
    print("1. Cook a Recipe")
    print("2. Display Pantry")
    print("3. Display Recipes")
    print("4. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        display_recipes()
        recipe_choice = input("Enter the name of the recipe you want to cook: ")
        cook_recipe(recipe_choice)
    elif choice == "2":
        display_pantry()
    elif choice == "3":
        display_recipes()
    elif choice == "4":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please select a valid option.")
