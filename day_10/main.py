import copy

# This code is veeeeeeery bad but i'm too lazy to fix it <3
# It works, so its gut


def move_cords(start_coords, direction):
    coords = list(start_coords)
    if direction == "up":
        coords[1] -= 1
    elif direction == "down":
        coords[1] += 1
    elif direction == "left":
        coords[0] -= 1
    elif direction == "right":
        coords[0] += 1

    if coords[0] < 0:
        coords[0] = 0

    if coords[1] < 0:
        coords[1] = 0
    return coords


def parse_distance_map(start_cords, direction):
    current_cords = start_cords
    distance = 0
    while True:
        current_cords = move_cords(list(current_cords), direction)
        current_value = pipes_map[current_cords[1]][current_cords[0]]

        possible_directions = [x for x in rotations_map[current_value] if x != reverse_directions[direction]][0]
        direction = possible_directions
        distance += 1

        if current_cords == list(start):
            break

        distances_map[current_cords[1]][current_cords[0]] = int(
            min(float(distance), distances_map[current_cords[1]][current_cords[0]]))


def part_one(distances_map):
    distances_map[start[1]][start[0]] = 0
    parse_distance_map(start, list(start_directions)[0])
    parse_distance_map(start, list(start_directions)[1])

    result = 0
    for row in distances_map:
        for cell in row:
            if cell != float('inf') and cell > result:
                result = cell

    return result


def part_two():
    def flood(flooded_map):
        new_map = copy.deepcopy(flooded_map)
        for x, x_list in enumerate(flooded_map):
            for y, state in enumerate(x_list):
                if state == "O":
                    flood_cell(y - 1, x, new_map)
                    flood_cell(y + 1, x, new_map)
                    flood_cell(y, x - 1, new_map)
                    flood_cell(y, x + 1, new_map)

        return new_map

    def flood_cell(x, y, flooded_map):
        try:
            if flooded_map[y][x] == ".":
                flooded_map[y][x] = "O"
        except:
            pass

    direction = start_directions[0]
    directions_map[start[1]][start[0]] = direction

    current_cords = start
    distance = 0
    while True:
        current_cords = move_cords(list(current_cords), direction)
        current_value = pipes_map[current_cords[1]][current_cords[0]]

        possible_directions = [x for x in rotations_map[current_value] if x != reverse_directions[direction]][0]
        direction = possible_directions
        distance += 1

        if current_cords == list(start):
            break

        directions_map[current_cords[1]][current_cords[0]] = direction

    bigger_map = []
    for x in directions_map:
        line = [".", "."]
        for y in x:
            line.append(y)
            line.append(".")
        line.append(".")
        line.append(".")
        bigger_map.append(line)
        bigger_map.append(["." for x in line])

    edited_bigger_map = copy.deepcopy(bigger_map)
    for x, x_list in enumerate(bigger_map):
        for y, direction in enumerate(x_list):
            if direction != ".":
                new_pos = move_cords((y, x), direction)
                edited_bigger_map[new_pos[1]][new_pos[0]] = direction

    edited_bigger_map[len(edited_bigger_map) - 1][len(edited_bigger_map[0]) - 1] = "O"

    for i in range(780):
        edited_bigger_map = flood(edited_bigger_map)

    result = 0
    for x in range(0, len(edited_bigger_map), 2):
        x_list = edited_bigger_map[x]
        for y in range(0, len(x_list), 2):
            if x_list[y] == ".":
                result += 1
    return result


if __name__ == "__main__":
    pipes_map = []
    distances_map = []
    directions_map = []
    start = (-1, -1)
    with open("./day_10/input.txt", 'r') as file:
        for y, line in enumerate(file):
            letters = []
            for x, letter in enumerate(line.strip()):
                letters.append(letter)
                if letter == "S":
                    start = x, y
            pipes_map.append(letters)
            distances_map.append([float('inf') for x in letters])
            directions_map.append(["." for x in letters])

    assert start != (-1, -1)

    rotations_map = {
        "L": ["right", "up"],
        "J": ["left", "up"],
        "F": ["down", "right"],
        "7": ["down", "left"],
        "|": ["down", "up"],
        "-": ["left", "right"]
    }
    reverse_directions = {
        "up": "down",
        "down": "up",
        "right": "left",
        "left": "right"
    }

    start_directions = []
    for direction in ["up", "down", "left", "right"]:
        reversed_direction = reverse_directions[direction]
        check_cords = move_cords(start, direction)
        value = pipes_map[check_cords[1]][check_cords[0]]
        keys = [key for key, value in rotations_map.items() if reversed_direction in value]
        if value in keys:
            start_directions.append(direction)

    symbol = next((key for key, value in rotations_map.items() if value == start_directions), None)
    pipes_map[start[1]][start[0]] = symbol

    print("---Part One---")
    print(part_one(distances_map))

    print("---Part Two---")
    print(part_two())
