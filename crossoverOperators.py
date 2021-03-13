import random

class uniformCrossover: #PL - jednolite/rownomierne
    CROSSOVER_CHANCE = 0.2
    @staticmethod
    def crossover(gen_1, gen_2):
        if len(gen_1) != len(gen_2):
            raise Exception("Crossover operator error")

        for i in range(len(gen_1)):
            if random.random() < uniformCrossover.CROSSOVER_CHANCE:
                buf = gen_1[i]
                gen_1[i] = gen_2[i]
                gen_2[i] = buf




