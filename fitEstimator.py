from direction import Direction
import collections

class fitEstimator:
    def estimate_fit_deviation(self, individual, goals, board_x, board_y):
        steps = self._create_steps(individual, goals)
        cross_amount = self._calc_cross_amount(steps)
        steps_amount = self._calc_steps_amount(steps)
        print("Cross amount = ", cross_amount)
        print("Steps amount = ", steps_amount)

    def _create_steps(self, individual, goals):
        steps = []
        for path, goal in zip(individual.paths, goals):
            start_position = goal[0]
            steps.append(start_position)
            for segment in path:
                segment_dir = segment[0]
                segment_lenght = segment[1]
                self._add_segment_to_steps_list(segment_dir, segment_lenght, steps)
        return steps

    def _add_segment_to_steps_list(self, segment_dir, segment_lenght, steps):
        if segment_dir == Direction.LEFT:
            for i in range(segment_lenght):
                current_step = (steps[-1][0] - 1, steps[-1][1])
                steps.append(current_step)

        elif segment_dir == Direction.RIGHT:
            for i in range(segment_lenght):
                current_step = (steps[-1][0] + 1, steps[-1][1])
                steps.append(current_step)

        elif segment_dir == Direction.UP:
            for i in range(segment_lenght):
                current_step = (steps[-1][0], steps[-1][1] - 1)
                steps.append(current_step)

        elif segment_dir == Direction.DOWN:
            for i in range(segment_lenght):
                current_step = (steps[-1][0], steps[-1][1] + 1)
                steps.append(current_step)

    def _calc_cross_amount(self, steps):
        cross_amount = 0
        occurrences = collections.Counter(steps)
        for occurence in occurrences.values():
            if occurence >= 2:          # to check if better "add blindly" or check if >=2 before.
                cross_amount = cross_amount + occurence - 1
        return cross_amount

    def _calc_steps_amount(self, steps):
        return len(steps)




estimator = fitEstimator()