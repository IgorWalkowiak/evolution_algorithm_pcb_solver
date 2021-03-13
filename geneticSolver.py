from individual import Individual
import fitEstimator
import selectionOperators
import crossoverOperators
import mutator
import random
import copy
from statistics import mean


class GeneticSolver():
    def __init__(self, population_amount, maxAttempts):
        self.estimator = fitEstimator.FitEstimator(1.0, 0.001, 4.0)
        self._population_amount = population_amount
        self._population = []
        self._maxAttempts = maxAttempts
        self.mutator = mutator.SingleStepMutator()

    def solve(self, problem):
        for _ in range(self._population_amount):
            self._population.append(Individual(problem.get_goals(), problem.board_x, problem.board_y, 3))

        for i in range(self._maxAttempts):
                generation_deviation = self._estimate_population(problem)

                self._population = selectionOperators.TournamentSelection.select(self._population, generation_deviation, 50)
                self._crossover_and_fill_population()
                self._mutate_population()

    def _estimate_population(self, problem):
        gen_estimation = []
        for individual in self._population:
            deviation = self.estimator.estimate_fit_deviation(individual, problem.get_goals(), problem.board_x, problem.board_y)
            gen_estimation.append(deviation)
        self._print_stats(gen_estimation)
        return gen_estimation

    def _crossover_and_fill_population(self):
        while len(self._population) != self._population_amount:
            new_individual = copy.deepcopy(random.choice(self._population))
            self._population.append(new_individual)

        for i in range(int(len(self._population) / 2)):
            crossoverOperators.uniformCrossover.crossover(self._population[i*2].paths, self._population[i*2 +1].paths)

    def _mutate_population(self):
        for individual in self._population:
            self.mutator.mutate(individual.paths)

    def _print_stats(self, estimations):
        print("best=", round(min(estimations),2) , ", avg=",round(mean(estimations),2), ", worst=", round(max(estimations),2))



