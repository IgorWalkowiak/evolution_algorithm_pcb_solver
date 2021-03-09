from direction import Direction
import mutator

import random


class Individual:
    def __init__(self, goals, board_x, board_y, startup_randomization):
        self.paths = []
        self._create_randomized_paths(goals, board_x, board_y, startup_randomization)

    def _create_randomized_paths(self, goals, board_x, board_y, startup_randomization):
        for goal in goals:
            random_path = self._create_random_path(goal, board_x, board_y, startup_randomization)
            self.paths.append(random_path)

        # Why I can't just do this?
        # for i in range(startup_randomization):
        #     mutator.singleStepMutator.mutate(self.paths)

    def _create_random_path(self, goal, board_x, board_y, startup_randomization):
        corners_amount = random.randint(0, startup_randomization)
        start = goal[0]
        finish = goal[1]
        #DEBUG _ START AND FINISH ACCESS
        #print("Start: ",start," Finish: ", finish)
        corners = self._create_corners(corners_amount, start, finish, board_x, board_y)
        return self._create_path_from_corners(corners)

    def _create_corners(self, corners_amount, start, finish, board_x, board_y):
        corners = [start]
        for _ in range(corners_amount):
            x_range = list(range(0, corners[-1][0])) + list(range(corners[-1][0]+1, board_x))
            x = random.choice(x_range)
            y_range = list(range(0, corners[-1][1])) + list(range(corners[-1][1]+1, board_y))
            y = random.choice(y_range)
            corners.append((x, y))
        corners.append(finish)
        return corners

    def _create_path_from_corners(self, corners):
        path = []
        for start, finish in zip(corners[:-1], corners[1:]):
            if start[0] > finish[0]:
                first_step = (Direction.LEFT, start[0] - finish[0])
                path.append(first_step)
            elif start[0] < finish[0]:
                first_step = (Direction.RIGHT, finish[0] - start[0])
                path.append(first_step)

            if start[1] > finish[1]:
                second_step = (Direction.UP, start[1] - finish[1])
                path.append(second_step)
            elif start[1] < finish[1]:
                second_step = (Direction.DOWN, finish[1] - start[1])
                path.append(second_step)
        #DEBUG _ PATH AND CORNERS ACCESS
        #print(corners)
        #print(path)
        #print("_____")
        return path









