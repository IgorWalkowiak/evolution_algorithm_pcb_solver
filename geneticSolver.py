from individual import Individual
from fitEstimator import estimator


class GeneticSolver():
    def __init__(self, population_number):
        self._population_number = population_number
        self._population = []

    def solve(self, problem):
        for _ in range(self._population_number):
            self._population.append(Individual(problem.get_goals()))

        for individual in self._population:
            deviation = estimator.estimate_fit_deviation(individual, problem.get_goals(), problem.board_x, problem.board_y)
            print(deviation)

