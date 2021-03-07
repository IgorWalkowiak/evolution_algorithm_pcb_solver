from individual import Individual
import fitEstimator


class GeneticSolver():
    def __init__(self, population_number):
        self.estimator = fitEstimator.FitEstimator(1.0, 0.01, 1.0)
        self._population_number = population_number
        self._population = []

    def solve(self, problem):
        for _ in range(self._population_number):
            self._population.append(Individual(problem.get_goals(), 1000000))

        for individual in self._population:
            deviation = self.estimator.estimate_fit_deviation(individual, problem.get_goals(), problem.board_x, problem.board_y)
            print(deviation)

