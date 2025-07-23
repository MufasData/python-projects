import os
from pathlib import Path

base_path = Path ( Path.home() / 'recipes' )

# recipe_path = Path( base_path / category )

category_path_list = list(base_path.glob('*'))

# recipe_path_list = list(recipe_path.glob('*'))

category_list = [ cat.stem for i,cat in enumerate(category_path_list) ]

# recipe_list = [ rec.stem for i,rec in enumerate(recipe_path_list) ]

recipe_count = 0

recipe_path_list = []

for cat in category_list:
    rec_path = Path( base_path / cat )


for cat in category_list:
    for rec in recipe_list:
        if Path( recipe_path / (rec + '.txt') ).exists() == True:
            recipe_count += 1

print(recipe_count)
print(category_list)
print(recipe_list)

print(f"""
    Hello! The path to the directory for all the recipes
    you are looking for is found in:
    {base_path}

    There are {recipe_count} total recipes in the folder.
    """)

def salutation():
    print("""
          
    Choose one of the options below:
    
    Option 1 - View a recipe
    Option 2 - Create a recipe
    Option 3 - Create a new category of recipes
    Option 4 - Delete a recipe
    Option 5 - Delete a category of recipes
    Option 6 - End the program

    """)

def category_pick():
    cat = input("Pick a category of meals you want?\n")
    return cat

def option_choice():
    choice = int(input("Choose an option...\n"))
    print()
    return choice



# def option_1(cat_list,rec_list):
#     cat = input("You have chosen option 1... Which category do you choose?\n")
#     if cat in cat_list:
#         rec = input("Now enter the meal for the recipe you want to prepare...\n")
#         if rec in rec_list:
#             file = open(
#         else:
#             return f"That meal is unavailable. Must be one of the following {str(rec_list)}"
#     else:
#         return f"That category does not exist. Must be one of the following {str(cat_list)}."
    
    


# choice = option_choice()

# while choice != 6:
#     if choice = 1:
