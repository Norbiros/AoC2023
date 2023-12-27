from math import lcm


def part_one(start, destination, directions, camel_map):
    position = start
    moves = 0
    while not position.endswith(destination):
        current_direction = directions[moves % len(directions)]
        index = 0 if current_direction == "L" else 1
        position = camel_map[position][index]
        moves += 1
    return moves, position


def part_two(directions, camel_map):
    start_positions = [x for x in camel_map.keys() if x.endswith("A")]
    moves = []
    for start_position in start_positions:
        move = part_one(start_position, "Z", directions, camel_map)
        moves.append(move[0])

    # FunFact: Moves from START to END == Moves from END to END (again)
    # Thx @reptilianeye (after I found my solution): length of cycle % instructions == 0
    print([(x, x % len(directions)) for x in moves])
    return lcm(*moves)


if __name__ == "__main__":
    input_data = []
    with open("./day_08/input.txt", 'r') as file:
        lines = file.readlines()
        camel_map_input = lines[2::]
        camel_map = {}
        for map_entry in camel_map_input:
            node, directions = map_entry.strip().split(" = ")
            camel_map[node] = directions.replace(")", "").replace("(", "").split(", ")

    print("---Part One---")
    print(part_one("AAA", "ZZZ", lines[0].strip(), camel_map)[0])

    print("---Part Two---")
    print(part_two(lines[0].strip(), camel_map))
