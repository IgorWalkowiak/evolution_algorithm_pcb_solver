from problem import Problem
from geneticSolver import GeneticSolver

if __name__ == '__main__':
    pr1 = Problem('zad0.txt')

    solver = GeneticSolver(2)
    solver.solve(pr1)
