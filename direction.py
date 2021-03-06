from enum import Enum

class Direction(Enum):
    UP = 0
    DOWN = 1
    RIGHT = 2
    LEFT = 3

def is_opposite_direction(dir1, dir2):
    if dir1 == Direction.UP and dir2 == Direction.DOWN:
        return True
    if dir1 == Direction.DOWN and dir2 == Direction.UP:
        return True
    if dir1 == Direction.LEFT and dir2 == Direction.RIGHT:
        return True
    if dir1 == Direction.RIGHT and dir2 == Direction.LEFT:
        return True

def get_opposite_direction(dir):
    if dir == Direction.UP:
        return Direction.DOWN
    if dir == Direction.DOWN:
        return Direction.UP
    if dir == Direction.LEFT:
        return Direction.RIGHT
    if dir == Direction.RIGHT:
        return Direction.LEFT