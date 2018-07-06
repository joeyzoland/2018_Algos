"""
Given a list of ingredients needed to bake one cake
And a list of total amount of ingredients available, predict what the maximum number of cakes will be

[2, 4, 1, 3] Ingredients per cake
[100, 80, 120, 60] Ingredients available for all cakes
"""

import math
def cakeMaker(recipe, ingredients):
    #Note: We're flooring because we're counting in whole cakes; if you don't have enough ingredients to make another full cake, those ingredients are wasted
    max = int(math.floor(ingredients[0] / recipe[0]))
    for i in range(1, len(recipe)):
        cakesPerIngredient = int(math.floor(ingredients[i] / recipe[i]))
        if cakesPerIngredient < max:
            max = cakesPerIngredient
    return max

recipeList = [2, 4, 1, 3]
ingredientList = [100, 80, 120, 58]
print(cakeMaker(recipeList, ingredientList))
