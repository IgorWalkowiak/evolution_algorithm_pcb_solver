SEPARATOR = ';'


class Problem:
    def __init__(self, dir):
        try:
            f = open(dir, encoding='utf-8')
            board_size = f.readline()
            self._add_coords(board_size)

            raw_goals = f.readlines()
            self.goals = []
            for raw_goal in raw_goals:
                parsed_goal = raw_goal.split(SEPARATOR)
                buf_goal = (
                    (int(parsed_goal[0]), int(parsed_goal[1])), (int(parsed_goal[2]), int(parsed_goal[3]))
                )
                self.goals.append(buf_goal)
        finally:
            f.close()

        print(self.board_x)
        print(self.board_y)
        print(self.goals)

    def _add_coords(self, board_size):
        self.board_x = int(board_size.split(SEPARATOR)[0])
        self.board_y = int(board_size.split(SEPARATOR)[1])

    def get_goals(self):
        return self.goals

    def get_board_x(self):
        return self.board_x

    def get_board_y(self):
        return self.board_y
