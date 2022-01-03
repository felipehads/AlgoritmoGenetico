#Cromossomo/Indivíduo: Combinação de Itens (30)
#Alelo: Presença ou ausência do Item
#Seleção(fitness): 
#Crossover/Cruzamento: 
#Mutação:
#Método da Roleta:

#Procedimento AG{ 
#   t = 0;
#   inicia_população (P, t)
#   avaliação (P, t);
#   repita até (t = d){ 
#     t = t +1;
#     seleção_dos_pais(P,t);
#     recombinação (P, t);
#     mutação (P, t);
#     avaliação (P, t);
#     sobrevivem (P, t)
#   }
#}
import numpy as np
from random import random, randint, getrandbits

# Geração de item, com 0(ausência) e 1(presença)
def itemCombination(number_of_items):
  return [ getrandbits(1) for x in range (number_of_items) ]

# Geração da população dos items
def generatePopulation(number_of_combinations, number_of_items):
  return [ itemCombination(number_of_items) for x in range(number_of_combinations) ]

# Função de avaliação realizada em cada item
def fitness(items, max_weight, max_cost, list_of_items):
  total_weight, total_cost, total_value = 0, 0, 0

  for index, value in enumerate(items):
    total_weight += (items[index] * list_of_items[index][0])
    total_cost += (items[index] * list_of_items[index][1])
    total_value += (items[index] * list_of_items[index][2])
  
  if ((total_weight > max_weight) or (total_cost > max_cost)):
    return -1

  return total_value

# Função que, através dos valores obtidos com a função anterior, retorna a média destes valores 
def average_fitness(items, max_weight, max_cost, list_of_items):
  # totalValue = 0
  
  # for item in items:
  #   if (fitness(item, max_weight, max_cost, list_of_items) >= 0):
  #     totalValue += fitness(item, max_weight, max_cost, list_of_items)

  sum_of_valid_fitness = sum(fitness(item, max_weight, max_cost, list_of_items) for item in items if fitness(item, max_weight, max_cost, list_of_items) >= 0)
  
  return sum_of_valid_fitness / (len(items))

def parents_selection(parents):

  # [(29, 34, 57, 10) , ('010100', '100100', '101010', '111001')] 
  values = list(zip(*parents))  
  # print(values)
  
  total_fitness = sum(values[0])

  # roulette, accumulation, sorted_value = [] , 0, random.uniform(0, total_fitness)

  def sort_index(total_fitness, last_index_selected = -1):

    if (last_index_selected != -1):
      total_fitness -= parents[0][last_index_selected]

    selection_probs = [(value/total_fitness) for value in values[0]]

  # for index, fitness_value in enumerate(values[0]):

    result = np.random.choice(values[1], p = selection_probs) 
    index = values[1].index(result)

    while (index == last_index_selected):
      result = np.random.choice(values[1], p = selection_probs) 
      index = values[1].index(result)

    return values[1].index(result)

    # if (last_index_selected == index):
    #   continue

    # accumulation += fitness_value

    # roulette.append(accumulation)


    # if(roulette[index] >= sorted_value):
    #   return index


  father_index = sort_index(total_fitness)
  mother_index = sort_index(total_fitness, father_index)

  father = values[1][father_index]
  mother = values[1][mother_index]

  return father, mother

# Função evolutiva
def evolve(items, max_weight, max_cost, list_of_items, number_of_combinations, mutate_percentage = 0.05):
  # Mapeia os fitness com seus valores binários
  parents = [[item] for item in items if fitness() ] 

  # print(parents)

  parents.sort(reverse=True)

  sons = []

  # Reprodução/Escolha dos pais
  # while len(sons) < number_of_combinations:
  #   father, mother = parents_selection(parents)

  #   middle = len(father) // 2
  #   son = father[:middle] + mother[middle:]
  #   sons.append(son)

  # # Mutação
  # for son in sons:
  #   if (mutate_percentage > random()):
  #     mutate_position = randint(0, len(son) -1)
  #     if (son[mutate_position] == 1):
  #       son[mutate_position] = 0
  #     else:
  #       son[mutate_position] = 1

  # return sons

  