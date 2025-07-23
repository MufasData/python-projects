import os
from pathlib import Path

def get_categories_list(base_path):
    cat_path_list = list(base_path.glob('*'))
    cat_list = [ cat.stem for i,cat in enumerate(cat_path_list)]
    return cat_list

def ask_category(cat_list):
    cat = input("Which category do you choose? " + ", ".join(cat_list) + '\n').capitalize()
    if cat in cat_list:
        return cat
    else:
        print("That category is not available.")
    
def get_recipe_list(base_path,category):
    recipe_path = Path( base_path / category )
    recipe_path_list = list(recipe_path.glob('*'))
    rec_list = [ rec.stem for i,rec in enumerate(recipe_path_list) ]
    return rec_list

def ask_recipe(rec_list):
    rec = input("Which recipe do you want to read? " + ", ".join(rec_list) + '\n').capitalize()
    if rec in rec_list:
        return rec
    else:
        print("That recipe is not available.")

def get_recipe_count(base_path,cat_list):
    count = 0
    for cat in cat_list:
        rec_path = Path( base_path / cat )
        rec_path_list = list(rec_path.glob('*'))
        rec_list = [ rec.stem for i,rec in enumerate(rec_path_list)]
        count += len(rec_list)
    return count

def salutation(base_path,recipe_count):
    print(f"""
          Hello! The path to the directory for all recipes
          you are looking for is found in:
          {base_path}
          
          There are {recipe_count} total recipes in the folder
          """)

def read_recipe(base_path,category,recipe):
    file_path = Path( base_path / category / (recipe + '.txt') )
    file = open(file_path)
    print(file.read())
    file.close()

# Main code
def main():

    base_path = Path( Path.home() / 'recipes' )
    category_list = get_categories_list(base_path)
    category = ask_category(category_list)

    recipe_list = get_recipe_list(base_path,category)
    recipe_count = get_recipe_count(base_path,category_list)
    recipe = ask_recipe(recipe_list)
    
    # print(category_list)
    # print(recipe_list)
    print("Recipe Count:", recipe_count)
    
    #salutation(base_path,recipe_count)




if __name__ == "__main__":
    main()