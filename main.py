#CONSOLE TO MANAGE RECIPES

recipes = [
{'cinnamon_cake': {'flour': 100, 'sugar': 1, 'eggs':1, 'milk':1, 'cinnamon':1}},
{'apple_cake':{'apple':2, 'flour':1, 'sugar':1, 'eggs':1, 'butter':1, 'vanille':1}},
{'cheese_cake': {'cheesecream':1, 'sugar': 1, 'eggs': 1, 'milk': 1, 'cookies': 1}},
{'banana_pancake':{'flour':1, 'banana':1, 'milk': 1}},
{'banana_milkshake':{'milk': 1, 'banana':1}},
{'smoothie':{'banana':1, 'apple':1, 'strawberry':2}},
{'cappuccino':{'milk':1, 'chocolate':1, 'coffee':1, 'cinnamon':1}},
{'cafe_con_leche': {'coffee':1, 'milk':1, 'sugar':1}}
]

def function(user_feedback):

    if user_feedback == "A":
        print ("Customer choice: List available recipes")
    elif user_feedback == "B":
        print ("Customer choice: List available recipes for one ingredient")
    elif user_feedback == "C":
        print ("Customer choice: List available recipes for two ingredients")
    elif user_feedback == "D":
        print ("Customer choice: List available recipes for three ingredients")

    #print("The user want to", user_feedback)


#As a user I want to be able to list all recipes
def list_recipes():
   for recipe in recipes:
    for recipe_name in recipe.keys():
           print ("Recipe's name: ", recipe_name)
           print ("Ingredients: ", recipe[recipe_name])
           print(" ")

def one_ingredient_recipes(customer_ingredient1):
    one_ingredient_recipes = []
    for recipe in recipes:
        for recipe_name in recipe.keys():
            for ingredient in recipe[recipe_name].keys():
                if ingredient == customer_ingredient1:
                    one_ingredient_recipes.append(recipe_name)
    print("You can prepare the listed recipe/s: ")
    print(one_ingredient_recipes)
    print("")


def two_ingredient_recipes(customer_ingredient1,customer_ingredient2):
    two_ingredients_recipes = []

    for recipe in recipes:
      for recipe_name in recipe.keys():
        this_recipe_has_the_ingredient_1 = False
        this_recipe_has_the_ingredient_2 = False
        if (this_recipe_has_the_ingredient_1 == False or this_recipe_has_the_ingredient_2 == False):
          for ingredient in recipe[recipe_name].keys():
            if(ingredient==customer_ingredient1):
                this_recipe_has_the_ingredient_1 = True

            if (ingredient == customer_ingredient2):
                this_recipe_has_the_ingredient_2 = True

        if (this_recipe_has_the_ingredient_1 == True and this_recipe_has_the_ingredient_2 == True):
          two_ingredients_recipes.append(recipe_name)

    print("You can prepare the listed recipe/s: ")
    print(two_ingredients_recipes)
    print ("")

def three_ingredient_recipes(customer_ingredient1,customer_ingredient2,customer_ingredient3):
    three_ingredients_recipes = []

    #customer_ingredient3 = str(input("Dear customer please insert ingredient three: "))
    for recipe in recipes:
      for recipe_name in recipe.keys():
        this_recipe_has_the_ingredient_1 = False
        this_recipe_has_the_ingredient_2 = False
        this_recipe_has_the_ingredient_3 = False
        if (this_recipe_has_the_ingredient_1 == False or this_recipe_has_the_ingredient_2 == False or this_recipe_has_the_ingredient_3 == False):
          for ingredient in recipe[recipe_name].keys():
            if(ingredient==customer_ingredient1):
              this_recipe_has_the_ingredient_1 = True

            if (ingredient == customer_ingredient2):
              this_recipe_has_the_ingredient_2 = True

            if (ingredient == customer_ingredient3):
              this_recipe_has_the_ingredient_3 = True

        if (this_recipe_has_the_ingredient_1 == True and this_recipe_has_the_ingredient_2 == True and this_recipe_has_the_ingredient_3 == True):
          three_ingredients_recipes.append(recipe_name)

    print("You can prepare the listed recipe/s: ")
    print(three_ingredients_recipes)
    print ("")

while True:
    user_feedback = input("Please choose one option A,B,C,D: ")
    function(user_feedback)



    if user_feedback == "A":
      list_recipes()
    elif user_feedback == "B":
      customer_ingredient1 = str(input("Please insert ingredient one: "))
      one_ingredient_recipes(customer_ingredient1)

    elif user_feedback == "C":
      customer_ingredient1 = str(input("Please insert ingredient one: "))
      customer_ingredient2 = str(input("Please insert ingredient two: "))
      two_ingredient_recipes(customer_ingredient1,customer_ingredient2)

    elif user_feedback == "D":
      customer_ingredient1 = str(input("Please insert ingredient one: "))
      customer_ingredient2 = str(input("Please insert ingredient two: "))
      customer_ingredient3 = str(input("Please insert ingredient three: "))
      three_ingredient_recipes(customer_ingredient1,customer_ingredient2,customer_ingredient3)
    else:
        print("option not available :)")


