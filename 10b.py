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

        ("S", Direction.UP): Direction.LEFT,
        ("S", Direction.RIGHT): Direction.DOWN,
    }

def is_start_position(tile):
    return tile == 'S'

def get_next_position(position: Position, direction: Direction) -> Position:
    dx, dy = direction.value
    return Position(position.x + dx, position.y + dy)

def do_single_step(previous_direction: Direction, current_position: Position, current_tile: str):
    next_direction = next_direction_map[current_tile, previous_direction]
    next_position = get_next_position(current_position, next_direction)
    next_tile = tiles[next_position.y][next_position.x]

    return next_direction, next_position, next_tile

def replace_tile(position: Position, previous_direction: Direction, next_direction: Direction):
    replacement_tile = "y" if previous_direction == Direction.DOWN or next_direction == Direction.UP else "x"
    tiles[position.y][position.x] = replacement_tile

def get_nr_enclosed_tiles():
    nr_enclosed_tiles = 0
    for row in tiles:
        in_loop = False
        for tile in row:
            if tile == "y":
                in_loop = not in_loop
            else:
                if in_loop and tile != "x":
                    nr_enclosed_tiles += 1

    return nr_enclosed_tiles

with open('10ainput.txt', 'r') as f:
    tiles = [list(line.strip()) for line in f]

    starting_position = Position(103, 20)
    previous_direction = Direction.LEFT

    current_position = get_next_position(starting_position, previous_direction)
    current_tile = tiles[current_position.y][current_position.x]
   
    while not is_start_position(current_tile):
        next_direction, next_position, next_tile = do_single_step(previous_direction, current_position, current_tile)
        replace_tile(current_position, previous_direction, next_direction)

        previous_direction = next_direction
        current_position = next_position
        current_tile = next_tile

    next_direction, next_position, next_tile = do_single_step(previous_direction, current_position, current_tile)
    replace_tile(current_position, previous_direction, next_direction)

    nr_enclosed_tiles = get_nr_enclosed_tiles()
    print(nr_enclosed_tiles)
