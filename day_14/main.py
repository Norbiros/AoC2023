import copy
from collections import defaultdict

def stack(rows_amount, data):
    for column in range(len(data[0])):
        for i in range(rows_amount):
            for row in range(rows_amount):
                if data[row][column] == "O" and row > 0 and data[row - 1][column] == ".":
                    data[row][column] = "."
                    data[row - 1][column] = "O"
    return data

def rotate(rows_amount, data):
    new_map = [[""] * rows_amount for _ in range(len(data[0]))]
    for row in range(rows_amount):
        for column in range(len(data[0])):
            new_map[column][rows_amount - row - 1] = data[row][column]
    return new_map


def part_one(data):
    rows_amount = len(data)

    stack(rows_amount, data)

    result = 0
    for row_id, row in enumerate(data):
        print("".join(row))
        for character in row:
            if character == "O":
                result += rows_amount - row_id
    return result

def part_two(data):
    i = 0
    rows_amount = len(data)
    current_data = copy.deepcopy(data)
    occurrences = defaultdict(lambda: [])
    while i < 10**9:
        i += 1

        for direction in range(4):
            current_data = stack(rows_amount, current_data)
            current_data = rotate(rows_amount, current_data)

        result = 0
        for row_id, row in enumerate(current_data):
            for character in row:
                if character == "O":
                    result += rows_amount - row_id

        if i >= 200:
            print(result, i, occurrences[result])
            # It repeats every 9, so 290, 299
            # (10**9-254)%9
            occurrences[result].append(i)


    result = 0
    for row_id, row in enumerate(data):
        print("".join(row))
        for character in row:
            if character == "O":
                result += rows_amount - row_id
    return result


# This code won't give you correct answer for part 2
# I calculate it manually based on occurrences
if __name__ == "__main__":
    data = []
    with open("./day_14/input.txt", 'r') as file:
        data = [[c for c in row.strip()] for row in file.readlines()]

    print("---Part One---")
    print(part_one(data))

    print("---Part Two---")
    print(part_two(data))
