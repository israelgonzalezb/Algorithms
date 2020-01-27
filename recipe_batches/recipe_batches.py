#!/usr/bin/python

import math
# First, we want to make sure that we have all the ingredients for the recipe... ie, maybe we need milk but there is no milk in the ingredients dictionary, so we can't make our food!
def recipe_batches(recipe, ingredients):
  recipe_keys = []
  ingredients_keys = []
  for item in recipe:
    recipe_keys.append(item)
  for item in ingredients:
    ingredients_keys.append(item)
  if len(recipe_keys) > len(ingredients_keys): # gotta have at least the same amount of types of ingredients
    return 0
  for i in recipe_keys: # check to see that we have at least some of all the ingredients needed for the recipe
    if i not in ingredients_keys:
      print(f"You're missing the ingredient: {i}")
      return 0
  batch = 0 # Init a var to hold max batches possible, and update in a loop based on modulo operation
  for item in recipe_keys:
    print(f"{item}: {recipe[item]} required, {ingredients[item]} on hand, you have enough for {round(ingredients[item]/recipe[item])} batches with this ingredient")
    if recipe[item] > ingredients[item]: # if at any point we have less of an ingredient than what the recipe requires, break out of the loop and return 0
      print(f"Need more {item}")
      return 0
    if batch == 0: # if this is the first iteration, set batch to the rounded product of the first ingredient item and recipe item
      batch = round(ingredients[item]/recipe[item])
    if round(ingredients[item]/recipe[item]) < batch: # if the rounded product of the current ingredient item and recipe item is less than the batch count we have, update batch to this lower number
      batch = round(ingredients[item]/recipe[item])
    print(f"Batch is {batch}")
  return batch
  pass 


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51}
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))