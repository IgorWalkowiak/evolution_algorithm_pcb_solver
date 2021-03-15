from problem import Problem
from geneticSolver import GeneticSolver
from randomSolver import RandomSolver
import mutator
import crossoverOperators
import fitEstimator
import selectionOperators

if __name__ == '__main__':
    pr1 = Problem('zad3.txt')

    ### SETTINGS ###
    MAX_ATTEMPTS = 100000

    CROSSING_ERROR_WEIGHT = 1.0
    STEP_ERROR_WEIGHT = 0.0001
    OUTER_STEP_ERROR_WEIGHT =5.0

    POPULATION_SIZE = 500
    PARENTS_POPULATION_RATIO = 0.5
    TOURNAMENT_SIZE_RATIO = 0.1
    #Good PARENTS/TOURNAMENT ration -> (0.4/0.5)

    CROSSOVER_CHANCE = 0.1

    MUTATE_CHANCE = 0.9
    MUTATE_MAX_LENGHT = 2
    ### SETTINGS ###

    fit_estimator = fitEstimator.FitEstimator(CROSSING_ERROR_WEIGHT, STEP_ERROR_WEIGHT, OUTER_STEP_ERROR_WEIGHT)
    selecton_operator = selectionOperators.TournamentSelection(TOURNAMENT_SIZE_RATIO)
   #selecton_operator = selectionOperators.RouletteSelection()
    crossover_operator = crossoverOperators.uniformCrossover(CROSSOVER_CHANCE)
    mutator_operator = mutator.StepMutator(MUTATE_CHANCE, MUTATE_MAX_LENGHT)
    solver = GeneticSolver(POPULATION_SIZE, MAX_ATTEMPTS, fit_estimator, selecton_operator, crossover_operator, mutator_operator, int(PARENTS_POPULATION_RATIO*POPULATION_SIZE))
    result = solver.solve(pr1)

    for path in result:
        print(path)

   # rand_solver = RandomSolver(1)
    #paths = rand_solver.solve(pr1)
    #print(paths)
