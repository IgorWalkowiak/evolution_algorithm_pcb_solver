import sys
sys.path.append('..') #Hack to import module from parent directory

import crossoverOperators


gen_A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gen_B = [11, 12, 13, 14, 15, 16, 17, 18, 19]

crossoverOperators.uniformCrossover.crossover(gen_A, gen_B)
print(gen_A)
print(gen_B)
