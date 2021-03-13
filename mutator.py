import direction as dirs
import random

MUTATE_CHANCE = 0.1


def random_mute_direction(direction):
    if direction == dirs.Direction.UP or direction == dirs.Direction.DOWN:
        if random.random() < 0.5:
            return dirs.Direction.LEFT
        else:
            return dirs.Direction.RIGHT
    else:
        if random.random() < 0.5:
            return dirs.Direction.UP
        else:
            return dirs.Direction.DOWN


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
        self._modify_step(step_num, path, mutation_start, mutation_end, direction_to_mutate)

    def _modify_step(self, step_num, path, mut_start, mut_end, dir):
        step_len = path[step_num][1]
        step_dir = path[step_num][0]
        del path[step_num]
        if mut_start != 0:
            path.insert(step_num, (step_dir, mut_start))
            step_num = step_num + 1
        if mut_end != step_len:
            path.insert(step_num+1, (step_dir, step_len - mut_end))
        path.insert(step_num, (step_dir, mut_end - mut_start))

        path.insert(step_num, (dir, 1))
        step_num = step_num + 1
        path.insert(step_num + 1, (dirs.get_opposite_turn(dir), 1))
        self._normalize(path, step_num)

    def _normalize(self, path, step_num):
        self._normalize_behind(path, step_num)
        self._normalize_before(path, step_num)
        self._check_normalization(path)

    def _normalize_before(self, path, step_num):
        if step_num >= 2:
            step_before_1 = step_num - 1
            step_before_2 = step_num - 2
            if dirs.is_same_way(path[step_before_2][0], path[step_before_1][0]):
                if dirs.is_opposite_turn(path[step_before_2][0], path[step_before_1][0]):
                    if path[step_before_2][1] > path[step_before_1][1]:
                        path[step_before_2] = (path[step_before_2][0], path[step_before_2][1] - path[step_before_1][1])
                        del path[step_before_1]
                    elif path[step_before_2][1] < path[step_before_1][1]:
                        path[step_before_2] = (path[step_before_1][0], path[step_before_1][1] - path[step_before_2][1])
                        del path[step_before_1]
                    else: #Direction are in opposite turn but equal
                        del path[step_before_1]
                        del path[step_before_2]
                else:
                    path[step_before_2] = (path[step_before_2][0], path[step_before_1][1] + path[step_before_2][1])
                    del path[step_before_1]

    def _normalize_behind(self, path, step_num):
        if step_num  <= len(path) - 3:
            step_behind_1 = step_num + 1
            step_behind_2 = step_num + 2
            if dirs.is_same_way(path[step_behind_2][0], path[step_behind_1][0]):
                if dirs.is_opposite_turn(path[step_behind_2][0], path[step_behind_1][0]):
                    if path[step_behind_2][1] > path[step_behind_1][1]:
                        path[step_behind_2] = (path[step_behind_2][0], path[step_behind_2][1] - path[step_behind_1][1])
                        del path[step_behind_1]
                    elif path[step_behind_2][1] < path[step_behind_1][1]:
                        path[step_behind_2] = (path[step_behind_1][0], path[step_behind_1][1] - path[step_behind_2][1])
                        del path[step_behind_1]
                    else: #Direction are in opposite turn but equal
                        del path[step_behind_2]
                        del path[step_behind_1]
                else:
                    path[step_behind_2] = (path[step_behind_2][0], path[step_behind_1][1] + path[step_behind_2][1])
                    del path[step_behind_1]

    def _check_normalization(self, path):
        for v, w, i in zip(path[:-1], path[1:], range(len(path))):
            if dirs.is_same_way(v[0], w[0]):
                if i == 0:
                    self._normalize_before(path, 2)
                    self._check_normalization(path)
                else:
                    self._normalize_behind(path, i-1)
                    self._check_normalization(path)
                break


singleStepMutator = SingleStepMutator()
