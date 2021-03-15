import random
from operator import itemgetter

class RouletteSelection:
    def select(self, population, fit_deviation, selected_amount):
        x = sum(fit_deviation)
        y = len(population) - 1 # as I try to minimalise es evaluation function I need some probability stuf
        roulett_chance = [(1-(deviation/x))/y for deviation in fit_deviation]
        roulett_chance = [ x**5 for x in roulett_chance ]
        winners = []
        while len(winners) != selected_amount:
            candidate = random.choices(population, weights=roulett_chance, k=1)
            if candidate[0] not in winners:
                winners.append(candidate[0])
        #DEBUG _ ROULLET_CHANCE AND ESTIMATION
        #print(roulett_chance, fit_deviation) #bigger fit_deviation -> smaller chance in roulett
        #print(population, winner) #bigger fit_deviation -> smaller chance in roulett
        return winners


class TournamentSelection:
    def __init__(self, tournament_size_ratio):
        self._tournament_size_ratio = tournament_size_ratio

    def select(self, population, fit_deviation, selected_amount):
        population_deviation = list(zip(population, fit_deviation))
        winners = []
        try:
            while len(winners) != selected_amount:
                for_tournament = random.sample(population_deviation, k=int(len(population_deviation)*self._tournament_size_ratio))
                winner = min(for_tournament, key=itemgetter(1))
                population_deviation.remove(winner)
                winners.append(winner[0])
        except:
            raise Exception("Tournament error. Probably wrong turnament settings")
        return winners






