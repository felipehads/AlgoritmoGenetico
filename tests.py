# frutas = ['Laranja', 'Uva', 'Maçã', 'Melancia']
# frutas2 = enumerate(frutas)
# for key, value in frutas2:
#   print("Indice:",key,"Valor: ",value)

import numpy as np
import random


# teste = [[12, '011111'], [20, '1001001'], [100,'100001'], [27,'010101']]
# sum_total = sum(x[0] for x in teste)
# teste_prob = [x[0]/sum_total for x in teste]
# values = [x[1] for x in teste]
# mulher = [0,0,0,0]
# meio = len(homem)//2
# filho = homem[:meio] + mulher[meio:]
# filho = list(zip(homem, homem))
# values = list(zip(*teste))
x = 0
# teste.sort(reverse=True)
# while (x < 10):
#   print(random.uniform(0, 60))
#   x += 1;
# for x in enumerate(values[1]):
#   print(x)
# for x in teste:
#   print(x)
# print(teste_prob)
# while x < 10:
#   result = np.random.choice(values, p = teste_prob)
#   print(result, "=", values.index(result))
#   x += 1

values = [(29, 34, 57, 100) , ('010100', '100100', '101010', '111001')]

total_fitness = sum(values[0])
# print(total_fitness)

# values = [ [0,1], [1,0], [1,1]]
# print(values)

selection_probs = [(value/total_fitness) for value in values[0] if value > 40]

print(selection_probs)

# while x < 10:
#   result = np.random.choice(values[0], p = selection_probs)
#   indice = values[0].index(result)
#   print(indice)
#   x+=1
