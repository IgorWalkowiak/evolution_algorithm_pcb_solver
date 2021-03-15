from individual import Individual
import random
import copy
from statistics import mean
import csv



class GeneticSolver():
    def __init__(self, population_amount, max_attempts, fit_estimator, selection_operator, crossover_operator, mutate_operator, parents_population):
        self._selection_operator = selection_operator
        self._parents_population = parents_population
        self._estimator = fit_estimator
        self._population_amount = population_amount
        self._population = []
        self._max_attempts = max_attempts
        self._crossover_operator = crossover_operator
        self._mutate_operator = mutate_operator
        self.successful_attempts_count = 0
        self.successful_attempts_MAX = 10




    def solve(self, problem):
        for _ in range(self._population_amount):
            self._population.append(Individual(problem.get_goals(), problem.board_x, problem.board_y, 3))

        for i in range(self._max_attempts):
                generation_deviation = self._estimate_population(problem)
                #self._print_best_in_population(generation_deviation)
                if self._is_good_enought_found():
                    return self._return_best_in_population(generation_deviation)
                self._population = self._selection_operator.select(self._population, generation_deviation, self._parents_population)
                self._crossover_and_fill_population()
                self._mutate_population()


        print("Algorithm hasn't found correct result :C")
        return self._return_best_in_population(generation_deviation)


    def _estimate_population(self, problem):
        gen_estimation = []
        individuals_status = []
        for individual in self._population:
            deviation, is_individual_ok = self._estimator.estimate_fit_deviation(individual, problem.get_goals(), problem.board_x, problem.board_y)
            gen_estimation.append(deviation)
            individuals_status.append(is_individual_ok)
        self._print_stats(gen_estimation)
        if any(individuals_status):
            print("DODAJE")
            self.successful_attempts_count = self.successful_attempts_count +1
        #self._save_stats(gen_estimation)
        return gen_estimation

    def _crossover_and_fill_population(self):
        while len(self._population) != self._population_amount:
            new_individual = copy.deepcopy(random.choice(self._population))
            self._population.append(new_individual)

        for i in range(int(len(self._population) / 2)):
            self._crossover_operator.crossover(self._population[i*2].paths, self._population[i*2 +1].paths)

    def _mutate_population(self):
        for individual in self._population:
            self._mutate_operator.mutate(individual.paths)

    def _print_stats(self, estimations):
        print("best=", round(min(estimations),2) , ", avg=",round(mean(estimations),2), ", worst=", round(max(estimations),2))

    def _save_stats(self, estimations):
        with open('logs.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([round(min(estimations),2), round(mean(estimations),2), round(max(estimations),2)])
            file.close()

    def _is_good_enought_found(self):
        if self.successful_attempts_count > self.successful_attempts_MAX:
            return True
        return False

    def _return_best_in_population(self, estimations):
        best_index = estimations.index(min(estimations))
        return self._population[best_index].paths

    def _print_best_in_population(self, estimations):
        best_index = estimations.index(min(estimations))
        for path in self._population[best_index].paths:
            print(path)






