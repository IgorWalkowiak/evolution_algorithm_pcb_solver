import random

class uniformCrossover: #PL - jednolite/rownomierne
    CROSSOVER_CHANCE = 0.2
    @staticmethod
    def crossover(genotype_1, genotype_2):
        if len(genotype_1) != len(genotype_2):
            raise Exception("Crossover operator error")

        for i in range(len(genotype_1)):
            if random.random() < uniformCrossover.CROSSOVER_CHANCE:
                buf = genotype_1[i]
                genotype_1[i] = genotype_2[i]
                genotype_2[i] = buf




