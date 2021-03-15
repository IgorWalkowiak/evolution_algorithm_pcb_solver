from direction import Direction
import collections

class FitEstimator:
    def __init__(self, cross_weight, step_weight, outer_step_weight):
        self.cross_weight = cross_weight
        self.step_weight = step_weight
        self.outer_step_weight = outer_step_weight


        ### Idea behind home made adaption is to turn on and off step penalty to let population grow in direct way in
        ### no "no penalty" state and then, when penalty is on again make that path shorter
        self._reset_step_weight_counter = 0
        self._reset_step_weight_trigger = -1 #if -1 then its disabled
        self._original_step_weight = step_weight


    def estimate_fit_deviation(self, individual, goals, board_x, board_y):
        steps = self._create_steps(individual, goals)
        cross_amount = self._calc_cross_amount(steps)
        steps_amount = self._calc_steps_amount(steps)
        outer_steps_amount = self._calc_outer_steps_amount(steps, board_x, board_y)

        is_ok = False
        if cross_amount==0 and outer_steps_amount==0:
            print("DODAJE")
            is_ok = True

        #DEBUG _ FIT PARAMETERS ACCESS
        #print("Cross= ", cross_amount, " , outer= ", outer_steps_amount, " , steps= ", steps_amount," , ind= ", individual)
        #print("Cross amount = ", cross_amount)
        #print("Steps amount = ", steps_amount)
        #print("Outer steps amount = ", outer_steps_amount)
        deviation = cross_amount*self.cross_weight + steps_amount*self.step_weight + outer_steps_amount*self.outer_step_weight
        self.handle_adaptation()
        return deviation, is_ok

    def handle_adaptation(self):
        self._reset_step_weight_counter = self._reset_step_weight_counter +1
        if self._reset_step_weight_counter == self._reset_step_weight_trigger:
            self._reset_step_weight_counter = 0
            if self.step_weight == 0.0:
                print("RESTORE")
                self.step_weight = self._original_step_weight
            else:
                print("SET 0")
                self.step_weight = 0.0


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

    def _calc_outer_steps_amount(self, steps, board_x, board_y):
        outer_steps_amount = 0
        for step in steps:
            if step[0] < 0 or step[0] >= board_x or step[1] < 0 or step[1] >= board_y:
                outer_steps_amount = outer_steps_amount + 1

        return outer_steps_amount
