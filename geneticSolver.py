from individual import Individual
import fitEstimator
import selectionOperators


class GeneticSolver():
    def __init__(self, population_number, maxAttempts):
        self.estimator = fitEstimator.FitEstimator(1.0, 0.01, 1.0)
        self._population_number = population_number
        self._population = []
        self._maxAttempts = maxAttempts

    def solve(self, problem):
        for _ in range(self._population_number):
            self._population.append(Individual(problem.get_goals(), problem.board_x, problem.board_y, 2))

        for _ in range(self._maxAttempts):
                generation_deviation = self._estimate_population(problem)
                self._population = selectionOperators.RouletteSelection.select(self._population, generation_deviation, 2)

    def _estimate_population(self, problem):
        gen_estimation = []
        for individual in self._population:
            deviation = self.estimator.estimate_fit_deviation(individual, problem.get_goals(), problem.board_x, problem.board_y)
            gen_estimation.append(deviation)
        return gen_estimation
