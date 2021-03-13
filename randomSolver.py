from individual import Individual
import fitEstimator


class RandomSolver():
    INITIAL_RANDOMIZATION = 6
    def __init__(self, population_number):
        self.estimator = fitEstimator.FitEstimator(1.0, 0.0, 1.0)
        self._population_number = population_number

    def solve(self, problem):
        solved = []
        while True:
            individual = Individual(problem.get_goals(), problem.board_x, problem.board_y, RandomSolver.INITIAL_RANDOMIZATION)
            deviation = self.estimator.estimate_fit_deviation(individual, problem.get_goals(), problem.board_x,
                                                              problem.board_y)
            if deviation <= 0.5: # less then 0.5 to avoid floats comparisions problem. Idea is where deviation == 0.0
                solved.append(individual.paths)
                if len(solved) == self._population_number:
                    return solved

