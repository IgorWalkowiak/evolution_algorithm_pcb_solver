import sys
sys.path.append('..') #Hack to import module from parent directory

import selectionOperators



print("Selection operator tests:")
print()

population = ['a', 'b', 'c', 'd', 'e']
deviation =  [  1, 100, 100,   1,  1] #bigger -> then smaller chance to pick

print("population: ", population)
print("deviation:  ", deviation)
tournament = selectionOperators.TournamentSelection(0.6)
result = tournament.select(population, deviation, 2)
print("tournament result: ", result)

roulette = selectionOperators.RouletteSelection()
result = roulette.select(population, deviation, 2)
print("roulette result: ", result)


print("_______")
print("END")
print("_______")
print("")
print("")
