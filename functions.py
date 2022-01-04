#Cromossomo/Indivíduo: Combinação de Itens (30)
#Alelo: Presença ou ausência do Item
#Seleção(fitness): 
#Crossover/Cruzamento: 
#Mutação:
#Método da Roleta:

#Procedimento AG { 
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
from random import random, randint, getrandbits

# Geração de combinação de itens individual, com 0(ausência) e 1(presença)
def itemCombination(number_of_items):
  return [ getrandbits(1) for x in range (number_of_items) ]

# Geração da população dos itens
def generatePopulation(number_of_combinations, number_of_items):
  return [ itemCombination(number_of_items) for x in range(number_of_combinations) ]

# Função de avaliação da utilidade da combinação de itens, só retorna a utilidade caso passe pelas restrições:
# Restrições: limite de 30kg (weight) / limite de R$100,00 (cost)
def fitness(item, max_weight, max_cost, list_of_items):
  total_weight, total_cost, total_value = 0, 0, 0

  for index, value in enumerate(item):
    total_weight += (item[index] * list_of_items[index][0])
    total_cost += (item[index] * list_of_items[index][1])
    total_value += (item[index] * list_of_items[index][2])
  
  if ((total_weight > max_weight) or (total_cost > max_cost)):
    return -1

  return total_value

# Função que, através dos valores obtidos com a função anterior, retorna a média das utilidades em certa geração
def average_fitness(items, max_weight, max_cost, list_of_items):
  
  sum_of_valid_fitness = sum(fitness(item, max_weight, max_cost, list_of_items) for item in items if fitness(item, max_weight, max_cost, list_of_items) >= 0)
  
  return sum_of_valid_fitness / (len(items))

# Função utilizada no processo evolutivo para selecionar os pais sorteados
def parents_selection(parents):

  # Checa se a quantidade de valores que passaram pelas restrições é maior ou igual a 2 (mínimo para realizar um cruzamento)
  if (len(parents) >= 2) :
  # [(29, 34, 57, 10) , ('010100', '100100', '101010', '111001')] 
    values = list(zip(*parents))  
    total_fitness = sum(values[0])
  else:
    father = itemCombination(30)
    mother = itemCombination(30)
    return father, mother


  def sort_index(total_fitness, last_index_selected = -1):
    roulette, accumulation, sorted_value = [] , 0, random()

    if (last_index_selected != -1):
      total_fitness -= values[0][last_index_selected]

    for index, fitness_value in enumerate(values[0]):

      if (last_index_selected == index):
        continue

      accumulation += fitness_value

      roulette.append(accumulation/total_fitness)

      if(roulette[-1] >= sorted_value):
        return index

  father_index = sort_index(total_fitness)
  mother_index = sort_index(total_fitness, father_index)

  father = values[1][father_index]
  mother = values[1][mother_index]

  return father, mother

# Função evolutiva: realizar o cruzamento e mutação da população
def evolve(items, max_weight, max_cost, list_of_items, number_of_combinations, mutate_percentage = 0.05):

  # Mapeia os fitness com seus valores binários
  # [(29, 34, 57, 10) , ('010100', '100100', '101010', '111001')]
  parents = [[fitness(item, max_weight, max_cost, list_of_items), item] for item in items if fitness(item, max_weight, max_cost, list_of_items) >= 0 ] 

  # [(57, 34, 29, 10) , ('010100', '100100', '101010', '111001')]
  parents.sort(reverse=True)

  sons = []

  # Reprodução/Escolha dos pais
  while len(sons) < number_of_combinations:
    father, mother = parents_selection(parents)

    middle = len(father) // 2
    son = father[:middle] + mother[middle:]
    sons.append(son)

  # Mutação
  for son in sons:
    if (mutate_percentage > random()):
      mutate_position = randint(0, len(son) -1)
      if (son[mutate_position] == 1):
        son[mutate_position] = 0
      else:
        son[mutate_position] = 1

  return sons

  