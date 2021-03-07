from direction import Direction
import mutator


class Individual:
    def __init__(self, goals, startup_randomization):
        self.paths = []
        self._create_randomized_paths(goals, startup_randomization)


    def _create_randomized_paths(self, goals, startup_randomization):
        for goal in goals:
            simplest_path = self._create_simplest_path(goal)
            self.paths.append(simplest_path)
        for i in range(startup_randomization):
            mutator.singleStepMutator.mutate(self.paths)

    def _create_simplest_path(self, goal):
        start = goal[0]
        finish = goal[1]
        simplest_path = []
        if start[0] > finish[0]:
            first_step = (Direction.LEFT, start[0] - finish[0])
            simplest_path.append(first_step)
        elif start[0] < finish[0]:
            first_step = (Direction.RIGHT, finish[0] - start[0])
            simplest_path.append(first_step)

        if start[1] > finish[1]:
            second_step = (Direction.UP, start[1] - finish[1])
            simplest_path.append(second_step)
        elif start[1] < finish[1]:
            second_step = (Direction.DOWN, finish[1] - start[1])
            simplest_path.append(second_step)
        return simplest_path






