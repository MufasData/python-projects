from pathlib import Path
import os
import shutil

recipe_folder = Path( os.getcwd() , 'Recipes' )

def number_of_recipes(folder):
    recipe_list = list(folder.glob("**/*.txt"))
    return len(recipe_list)

num_of_recipes = number_of_recipes(recipe_folder)

def get_category_list():
    category_list = [ cat.stem for i,cat in enumerate(list(recipe_folder.glob("*"))) ]
    return category_list

def category_choice():
    category = input("Choose a category... ")
    return category

def get_recipe_list(cat):
    recipe_list = [ rec.stem for i,rec in enumerate(list(Path(recipe_folder, cat).glob("*"))) ]
    return recipe_list

def recipe_choice():
    recipe = input("Choose a recipe...")
    return recipe

def greeting():
    print(f"""
    Welcome!
          
    The path to the recipes 
    you are looking for is:
    {recipe_folder}

    There are {num_of_recipes} recipes in the recipes folder.
    """)

def program_choice():
    choice = input(f"""
    Please make a choice for what you want to do:
    
    1) Read a recipe
    2) Create a recipe
    3) Create a category
    4) Delete a recipe
    5) Delete a category
    6) End the program
    """)

    return choice

def option1():
    category = category_choice()
    category_list = get_category_list()
    if category not in category_list:
        return "Sorry, that is not a category."
    else:
        recipe_list = get_recipe_list(category)
        recipe = recipe_choice()
        if recipe not in recipe_list:
            return "Sorry, that is not an available recipe."
        else:
            return Path(recipe_folder,category,recipe + '.txt').read_text()

def option2():
    category = category_choice()
    category_list = get_category_list()
    if category not in category_list:
        return "Sorry, that is not a category."
    else:
        recipe_name = input("What is the recipe you want to create? ") + '.txt'
        file_path = Path(recipe_folder/category/recipe_name)
        content = input("Put the recipe here\n")
        with file_path.open("w") as f:
            f.write(content)
        return "Done."
        
def option3():
    new_category = input("What is the name of the new category you want to add? ")
    os.makedirs(Path(recipe_folder/new_category))
    return "Done"

def option4():
    category = category_choice()
    category_list = get_category_list()
    if category not in category_list:
        return "Sorry, that is not a category."
    else:
        recipe_list = get_recipe_list(category)
        recipe = recipe_choice()
        if recipe not in recipe_list:
            return "Sorry, that is not an available recipe."
        else:
            Path(recipe_folder/category/(recipe+'.txt')).unlink()
            return "Done."

def option5():
    category_del = input("What category do you want deleted? ")
    # Can use shutil.rmtree to remove a diretory with files in it. Library is imported above
    os.rmdir(recipe_folder/category_del)
    return "Done."
# Main body of code
greeting()

while True:
    program_num = program_choice()
    os.system('cls')
    if program_num == '1':
        print(option1())
    elif program_num == '2':
        print(option2())
    elif program_num == '3':
        print(option3())
    elif program_num == '4':
        print(option4())
    elif program_num == '5':
        print(option5())
    elif program_num == '6':
        print("Thank you for interacting. Program shutting down...")
        break
    else:
        print("Improper entry, try again.")