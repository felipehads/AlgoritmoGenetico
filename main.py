from functions import *


# [(29, 34, 57, 10) , ('010100', '100100', '101010', '111001')]
list_of_items = [[5,10,1], [2,15,1], [7,2,3], [7,5,1], [6,15,2], [2,16,4], [3,2,4], [1,8,2], [2,7,5], [3,15,1], [4,16,1], [7,2,5], [1,14,1], [1,13,5], [4,8,2], [8,5,2], [5,1,2], [8,13,5], [2,20,3], [4,9,3], [6,5,1], [8,4,1], [5,12,5], [4,7,4], [7,11,2], [8,17,4], [8,1,3], [6,10,4], [1,11,4], [3,6,5]]

max_weight = 30
max_cost = 100

number_of_combinations = 5
generations = 80
number_of_items = len(list_of_items)
# print(number_of_items)

# print(itemCombination(30))
# [0, [1,1,0,0,1]]
# [1, [0,0,1,0,1]]
items = generatePopulation(number_of_combinations, number_of_items)
# for item in enumerate(items):
#   print(item)
# print(items)
fitness_history = [average_fitness(items, max_weight, max_cost, list_of_items)]

# print(fitness_history)

# average_fitness()

for i in range(generations):
  evolve(items, max_weight, max_cost, list_of_items, number_of_combinations)
  fitness_history.append(average_fitness(items, max_weight, max_cost, list_of_items))

# for index, data in enumerate(fitness_history):
#   print("Generation: ", index, " | Average value:", data)