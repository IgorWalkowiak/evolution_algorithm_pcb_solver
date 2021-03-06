from individual import Individual

class GeneticSolver():
    def __init__(self, population_number):
        self._population_number = population_number
        self._population = []

    def solve(self, problem):
        for _ in range(self._population_number):
            self._population.append(Individual(problem.get_goals()))

