import sys
sys.path.append('..') #Hack to import module from parent directory

import crossoverOperators


genotype_A = [1, 2, 3, 4, 5, 6, 7, 8, 9]
genotype_B = [11, 12, 13, 14, 15, 16, 17, 18, 19]
crossover_operator = crossoverOperators.uniformCrossover(0.1)

print("Crossover operator tests:")
print()

print("Before crossover genotype A :", genotype_A, ", genotype B :", genotype_B)

crossover_operator.crossover(genotype_A, genotype_B)
print("After crossover genotype A :", genotype_A, ", genotype B :", genotype_B)

print("_______")
print("END")
print("_______")
print("")
print("")
