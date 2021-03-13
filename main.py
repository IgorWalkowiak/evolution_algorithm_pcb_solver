from problem import Problem
from geneticSolver import GeneticSolver
from randomSolver import RandomSolver
if __name__ == '__main__':
    pr1 = Problem('zad3.txt')

    solver = GeneticSolver(100, 10000)
    solver.solve(pr1)

   # rand_solver = RandomSolver(1)
    #paths = rand_solver.solve(pr1)
    #print(paths)
