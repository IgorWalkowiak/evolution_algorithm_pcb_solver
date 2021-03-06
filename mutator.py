from direction import Direction
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
        direction_to_mutate = random_mute_direction(step_dir)
        print(step_dir)
        print(direction_to_mutate)

singleStepMutator = SingleStepMutator()