import sys
sys.path.append('..') #Hack to import module from parent directory

import crossoverOperators


genotype_A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
genotype_B = [11, 12, 13, 14, 15, 16, 17, 18, 19]

crossoverOperators.uniformCrossover.crossover(genotype_A, genotype_B)
print(genotype_A)
print(genotype_B)
