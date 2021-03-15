import sys
sys.path.append('..') #Hack to import module from parent directory

import mutator
import direction


print("Mutation operator tests:")
print()

path = [[(direction.Direction.DOWN, 5)]]
print("Path before mutation: ", path)

mutate_operator = mutator.StepMutator(0.5, 1)
mutate_operator.mutate(path)
print("Path after mutation: ", path)



print("_______")
print("END")
print("_______")
print("")
print("")

