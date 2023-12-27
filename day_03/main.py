import copy
from collections import defaultdict
from typing import List


def get_substring(lst, index):
    if index < 0 or index >= len(lst) or lst[index] == '.':
        return ""

    left_index = index
    while left_index >= 0 and lst[left_index].isnumeric():
        left_index -= 1

    right_index = index
    while right_index < len(lst) and lst[right_index].isnumeric():
        right_index += 1

    substring = lst[left_index + 1:right_index]

    return substring


def part_one(board: List[List[str]]) -> int:
    real_board = copy.deepcopy(board)
    result = 0
    previous_val = None
    for y, x_list in enumerate(board):
        for x, current_value in enumerate(x_list):
            x = int(x)
            y = int(y)
            if current_value.isdigit():
                positions_to_check = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
                for position in positions_to_check:
                    check_x, check_y = position
                    check_x += x
                    check_y += y

                    if check_x < 0 or check_x >= len(x_list) or check_y < 0 or check_y >= len(board):
                        continue

                    symbol = board[check_y][check_x]
                    if symbol != "." and not symbol.isdigit() and not symbol.isalpha() and previous_val == None:
                        amount = int("".join(get_substring(real_board[y], x)))
                        result += amount
                        previous_val = amount
            else:
                previous_val = None

    return result


def part_two(board: List[List[str]]) -> int:
    real_board = copy.deepcopy(board)
    result = 0
    previous_val = None

    colliders = defaultdict(lambda: [])
    for y, x_list in enumerate(board):
        for x, current_value in enumerate(x_list):
            x = int(x)
            y = int(y)
            if current_value.isdigit():
                positions_to_check = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]
                for position in positions_to_check:
                    check_x, check_y = position
                    check_x += x
                    check_y += y

                    if check_x < 0 or check_x >= len(x_list) or check_y < 0 or check_y >= len(board):
                        continue

                    symbol = board[check_y][check_x]
                    if symbol == "*" and previous_val is None:
                        amount = int("".join(get_substring(real_board[y], x)))
                        colliders[f"{check_x}.{check_y}"].append(amount)
                        previous_val = amount
                        board[int(y)][int(x)] = "X"

                if board[y][int(x)] != "X":
                    board[y][int(x)] = "N"
            else:
                previous_val = None

    for collider_position, collider in colliders.items():
        if len(collider) == 2:
            result += collider[0] * collider[1]
    return result


if __name__ == "__main__":
    with open("./day_03/input.txt", 'r') as file:
        input_lines = [line.strip() for line in file]

    board = []
    for line in input_lines:
        board.append(list(line))

    print("---Part One---")
    print(part_one(board))

    print("---Part Two---")
    print(part_two(board))
