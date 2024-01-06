from collections import namedtuple
from enum import Enum

Position = namedtuple('Position', ['x', 'y'])

class Direction(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

next_direction_map = {
        ("|", Direction.UP): Direction.UP,
        ("|", Direction.DOWN): Direction.DOWN,
        ("-", Direction.LEFT): Direction.LEFT,
        ("-", Direction.RIGHT): Direction.RIGHT,
        ("L", Direction.DOWN): Direction.RIGHT,
        ("L", Direction.LEFT): Direction.UP,
        ("J", Direction.DOWN): Direction.LEFT,
        ("J", Direction.RIGHT): Direction.UP,
        ("7", Direction.UP): Direction.LEFT,
        ("7", Direction.RIGHT): Direction.DOWN,
        ("F", Direction.UP): Direction.RIGHT,
        ("F", Direction.LEFT): Direction.DOWN,
    }

def is_start_position(tile):
    return tile == 'S'

with open('10ainput.txt', 'r') as f:
    tiles = [list(line.strip()) for line in f]

    current_tile = "F"
    previous_direction = Direction.LEFT
    current_position = Position(102, 20)
    nr_steps = 1
    
    while not is_start_position(current_tile):
        next_direction = next_direction_map[current_tile, previous_direction]
        dx, dy = next_direction.value
        next_position = Position(current_position.x + dx, current_position.y + dy)
        next_tile = tiles[next_position.y][next_position.x]

        current_tile = next_tile
        previous_direction = next_direction
        current_position = next_position

        nr_steps += 1

    distance = int(nr_steps/2)

    print(distance)