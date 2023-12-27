import sys
from collections import defaultdict


def move_in_direction(direction, position):
    if direction == 0:
        return position[0], position[1] - 1
    elif direction == 1:
        return position[0] + 1, position[1]
    elif direction == 2:
        return position[0], position[1] + 1
    elif direction == 3:
        return position[0] - 1, position[1]


def light_beam(position, direction, filled_board, board):
    if position[0] < 0 or position[0] >= len(board[0]) or position[1] < 0 or position[1] >= len(board):
        return

    if seen[(position[0], position[1], direction)]:
        return

    seen[(position[0], position[1], direction)] = True

    if board[position[1]][position[0]] == ".":
        light_beam(move_in_direction(direction, position), direction, filled_board, board)
    elif board[position[1]][position[0]] == "|" and (direction in [1, 3]):
        direction_up = 0
        light_beam(move_in_direction(direction_up, position), direction_up, filled_board, board)

        direction_down = 2
        light_beam(move_in_direction(direction_down, position), direction_down, filled_board, board)
    elif board[position[1]][position[0]] == "|" and (direction in [0, 2]):
        light_beam(move_in_direction(direction, position), direction, filled_board, board)

    elif board[position[1]][position[0]] == "-" and (direction in [0, 2]):
        direction_left = 3
        light_beam(move_in_direction(direction_left, position), direction_left, filled_board, board)

        direction_right = 1
        light_beam(move_in_direction(direction_right, position), direction_right, filled_board, board)
    elif board[position[1]][position[0]] == "-" and (direction in [1, 3]):
        light_beam(move_in_direction(direction, position), direction, filled_board, board)
    elif board[position[1]][position[0]] == "/":
        if direction == 0:
            new_direction = 1
        elif direction == 1:
            new_direction = 0
        elif direction == 2:
            new_direction = 3
        elif direction == 3:
            new_direction = 2
        else:
            assert False

        light_beam(move_in_direction(new_direction, position), new_direction, filled_board, board)
    elif board[position[1]][position[0]] == "\\":
        if direction == 0:
            new_direction = 3
        elif direction == 1:
            new_direction = 2
        elif direction == 2:
            new_direction = 1
        elif direction == 3:
            new_direction = 0
        else:
            assert False
        light_beam(move_in_direction(new_direction, position), new_direction, filled_board, board)

    filled_board[position[1]][position[0]] = "#"


def part_one(data, position, direction):
    seen.clear()
    # 0 - up, 1 - right, 2 - down, 3 - left
    filled_board = [["." for _ in x] for x in data]

    light_beam(position, direction, filled_board, data)

    result = 0
    for x in filled_board:
        for y in x:
            if y == "#":
                result += 1
    return result


def part_two(data):
    result = 0
    for x_index, x in enumerate(data):
        result = max(part_one(data, (0, x_index), 1), result)
        result = max(part_one(data, (len(x) - 1, x_index), 3), result)

    for y_index, y in enumerate(data[0]):
        result = max(part_one(data, (y_index, 0), 2), result)
        result = max(part_one(data, (y_index, len(data) - 1), 0), result)

    return result


if __name__ == "__main__":
    sys.setrecursionlimit(5000)

    seen = defaultdict(lambda: False)
    with open("./day_16/input.txt", 'r') as file:
        data = [[y for y in x.strip()] for x in file.readlines()]

    print("---Part One---")
    print(part_one(data, (0, 0), 1))

    print("---Part Two---")
    print(part_two(data))
