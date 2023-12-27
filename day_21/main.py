
def part_one(garden, start_x, start_y, input_amount):
    positions_to_check = [(start_x, start_y)]

    for i in range(input_amount):
        # print(positions_to_check)
        new_positions_to_check = set()
        for position in positions_to_check:
            x, y = position
            for new_x, new_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if new_y < 0 or new_y >= len(garden) or new_x < 0 or new_x >= len(garden[0]) or garden[new_y][new_x] == "#":
                    continue
                new_positions_to_check.add((new_x, new_y))
        positions_to_check = list(new_positions_to_check)

    return len(positions_to_check)

def part_two(garden, amount):
    result = 0
    start_x = start_y = 65
    size = len(garden)
    grid_width = amount // size - 1
    odd_amount = (grid_width // 2 * 2 + 1) ** 2 # Without middle
    even_amount = ((grid_width + 1) // 2 * 2) ** 2

    points_in_odd = part_one(garden, start_x, start_y, len(garden) * 2 + 1)
    points_in_even = part_one(garden, start_x, start_y, len(garden) * 2 + 2)
    result += odd_amount * points_in_odd
    result += even_amount * points_in_even

    corners = [
        part_one(garden, start_x, size - 1, size - 1),
        part_one(garden, 0, start_y, size - 1),
        part_one(garden, start_x, 0, size - 1),
        part_one(garden, size - 1, start_y, size - 1)
    ]
    result += sum(corners)

    small_diagnoal_parts = [
        part_one(garden, 0, size - 1, size // 2 - 1),
        part_one(garden, size - 1, size - 1, size // 2 - 1),
        part_one(garden, 0, 0, size // 2 - 1),
        part_one(garden, size - 1, 0, size // 2 - 1)
    ]
    for part in small_diagnoal_parts:
        result += (grid_width + 1) * part

    big_diagnoal_part = [
        part_one(garden, 0, size - 1, (size * 3) // 2 - 1),
        part_one(garden, size - 1, size - 1, (size * 3) // 2 - 1),
        part_one(garden, 0, 0, (size * 3) // 2 - 1),
        part_one(garden, size - 1, 0, (size * 3) // 2 - 1)
    ]
    for part in big_diagnoal_part:
        result += grid_width * part



    return result

if __name__ == "__main__":
    garden = []

    with open("./day_21/input.txt", 'r') as file:
        for line in file:
            garden.append(list(line.strip()))


    print("---Part One---")
    print(part_one(garden, 65, 65, 64))

    print("---Part Two---")
    print(part_two(garden, 26501365))
