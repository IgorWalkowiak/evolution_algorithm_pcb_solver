from problem import Problem
from geneticSolver import GeneticSolver

if __name__ == '__main__':
    pr1 = Problem('test0.txt')

    solver = GeneticSolver(1)
    solver.solve(pr1)
