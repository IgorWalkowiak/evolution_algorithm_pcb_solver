from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 10
    RIGHT = 100
    LEFT = 1000

def is_same_way(dir1, dir2):
    dir_sum = dir1.value + dir2.value
    if dir_sum in [2, 11, 20, 200, 1100, 2000]:
        return True

def is_opposite_turn(dir1, dir2):
    dir_sum = dir1.value + dir2.value
    if dir_sum in [11, 1100]:
        return True

def get_opposite_turn(dir):
    if dir == Direction.UP:
        return Direction.DOWN
    if dir == Direction.DOWN:
        return Direction.UP
    if dir == Direction.LEFT:
        return Direction.RIGHT
    if dir == Direction.RIGHT:
        return Direction.LEFT