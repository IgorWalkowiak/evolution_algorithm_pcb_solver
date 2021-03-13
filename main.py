from problem import Problem
from geneticSolver import GeneticSolver
from randomSolver import RandomSolver
if __name__ == '__main__':
    pr1 = Problem('zad1.txt')

    solver = GeneticSolver(3, 5)
    solver.solve(pr1)

   # rand_solver = RandomSolver(1)
    #paths = rand_solver.solve(pr1)
    #print(paths)
