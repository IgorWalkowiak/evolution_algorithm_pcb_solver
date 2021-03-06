from direction import Direction
from direction import is_opposite_direction
from direction import get_opposite_direction
import random

MUTATE_CHANCE = 1.0


def random_mute_direction(direction):
    if direction == Direction.UP or direction == Direction.DOWN:
        if random.random() < 0.5:
            return Direction.LEFT
        else:
            return Direction.RIGHT
    else:
        if random.random() < 0.5:
            return Direction.UP
        else:
            return Direction.DOWN


class SingleStepMutator:
    def mutate(self, paths):
        if random.random() <= MUTATE_CHANCE:
            path_num_to_mutate = random.randint(0, len(paths) - 1)
            self._mutate_specific_path(paths[path_num_to_mutate])

    def _mutate_specific_path(self, path):
        step_num_to_mutate = random.randint(0, len(path) - 1)
        self._mutate_specific_step(step_num_to_mutate, path)

    def _mutate_specific_step(self, step_num, path):
        step = path[step_num]
        step_dir, step_len = step[0], step[1]
        if step_len == 1:
            mutation_start = 0
            mutation_end = 1
        else:
            mutation_start = random.randint(0, step_len - 2)
            mutation_end = random.randint(mutation_start + 1, step_len)
        direction_to_mutate = random_mute_direction(step_dir)


        print("PRZED: ", path)
        print("Dotyczy step_num: ",step_num)
        print('')
        self._modify_step(step_num, path, mutation_start, mutation_end, direction_to_mutate)
        print("PO: ", path)
        print('')

    def _modify_step(self, step_num, path, mut_start, mut_end, dir):
        print('mut_start: ', mut_start)
        print('mut_end: ', mut_end)
        print('mut_dir: ', dir)
        step_len = path[step_num][1]
        step_dir = path[step_num][0]
        del path[step_num]
        if mut_start != 0:
            path.insert(step_num, (step_dir, mut_start))
            step_num = step_num + 1
        print("PATH1: ", path)
        if mut_end != step_len:
            path.insert(step_num+1, (step_dir, step_len - mut_end))
        print("PATH2: ", path)
        print("PATH3: ", path)
        path.insert(step_num, (step_dir, mut_end - mut_start))
        print("PATH4: ", path)

        path.insert(step_num, (dir, 1))
        print("PATH5: ", path)
        step_num = step_num + 1
        path.insert(step_num + 1, (get_opposite_direction(dir), 1))
        print("PATH6: ", path)








singleStepMutator = SingleStepMutator()