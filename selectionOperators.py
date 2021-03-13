import random

class RouletteSelection:
    CROSSOVER_CHANCE = 0.2
    @staticmethod
    def select(population, fit_deviation, selected_amount):
        x = sum(fit_deviation)
        y = len(population) - 1 # as I try to minimalise es evaluation function I need some probability stuf
        roulett_chance = [(1-(deviation/x))/y for deviation in fit_deviation]

        #DEBUG _ ROULLET_CHANCE AND ESTIMATION
        print(roulett_chance, fit_deviation) #bigger fit_deviation -> smaller chance in roulett

        winner = []
        while len(winner) != selected_amount:
            candidate = random.choices(population, weights=roulett_chance, k=1)
            if candidate not in winner:
                winner.append(candidate)

        return winner






class TournamentSelection:
    pass





