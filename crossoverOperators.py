import random

class uniformCrossover: #PL - jednolite/rownomierne
    def __init__(self, crossover_chance):
        self._crossover_chance = crossover_chance

    def crossover(self, genotype_1, genotype_2):
        if len(genotype_1) != len(genotype_2):
            raise Exception("Crossover operator error")

        for i in range(len(genotype_1)):
            if random.random() < self._crossover_chance:
                buf = genotype_1[i]
                genotype_1[i] = genotype_2[i]
                genotype_2[i] = buf




