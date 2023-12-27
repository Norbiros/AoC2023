import copy
import sys
from collections import defaultdict


def move(point, start, end_points, forest, visited, length):
    position = start

    possible_moves = []
    for to_move in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        pos_to_check = (position[0] + to_move[0], position[1] + to_move[1])

        if pos_to_check[0] < 0 or pos_to_check[0] >= width or pos_to_check[1] < 0 or pos_to_check[1] >= height:
            continue

        block = forest[pos_to_check[1]][pos_to_check[0]]
        if pos_to_check in visited or block == "#":
            continue

        possible_moves.append(pos_to_check)

    new_visited = visited + [position]

    for pos in possible_moves:
        if pos in end_points:
            graph[point][pos] = length + 1
        else:
            move(point, pos, end_points, forest, new_visited, length + 1)


def part_two():

    interesting = [start, end]

    for y, row in enumerate(forest):
        for x, symbol in enumerate(row):
            if symbol == "#":
                continue
            near = 0
            position = x, y
            for to_move in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
                pos_to_check = (position[0] + to_move[0], position[1] + to_move[1])
                if pos_to_check[0] < 0 or pos_to_check[0] >= width or pos_to_check[1] < 0 or pos_to_check[1] >= height:
                    continue

                block = forest[pos_to_check[1]][pos_to_check[0]]
                if block == "#":
                    continue
                near += 1

            if near >= 3:
                interesting.append((x, y))

    for point in interesting:
        move(point, point, interesting, forest, [], 0)

    seen = set()
    def dfs(pt):
        if pt == end:
            return 0

        m = -float("inf")

        seen.add(pt)
        for nx in graph[pt]:
            if nx not in seen:
                m = max(m, dfs(nx) + graph[pt][nx])
        seen.remove(pt)

        return m
    return dfs(start)


def move_part_one(position, forest, length, visited):
    new_length = 0

    moved = False
    for to_move in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
        pos_to_check = (position[0] + to_move[0], position[1] + to_move[1])

        if pos_to_check[0] < 0 or pos_to_check[0] >= len(forest[0]) or pos_to_check[1] < 0 or pos_to_check[1] >= len(
                forest):
            continue

        block = forest[pos_to_check[1]][pos_to_check[0]]
        if pos_to_check in visited or block == "#":
            continue

        if block == ">" and to_move == (-1, 0):
            continue
        if block == "<" and to_move == (1, 0):
            continue
        if block == "^" and to_move == (0, 1):
            continue
        if block == "v" and to_move == (0, -1):
            continue

        new_visited = copy.copy(visited)
        new_visited.append(pos_to_check)

        moved_length = move_part_one(pos_to_check, forest, length + 1, new_visited)

        new_length = max(moved_length, new_length)
        moved = True

    if not moved and position[1] + 1 != len(forest):
        return -1

    if not moved:
        global part_one_answer
        part_one_answer = max(part_one_answer, length)
    return new_length


if __name__ == "__main__":
    sys.setrecursionlimit(5000)
    graph = defaultdict(lambda: {})

    with open("./day_23/input.txt", 'r') as file:
        forest = [list(row.strip()) for row in file.readlines()]

    start = (forest[0].index("."), 0)
    end = (forest[-1].index("."), len(forest) - 1)

    height = len(forest)
    width = len(forest[0])

    print("---Part One---")
    part_one_answer = 0
    move_part_one(start, forest, 0, [start])
    print(part_one_answer)

    print("---Part Two---")
    print(part_two())
