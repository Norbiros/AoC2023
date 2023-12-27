import copy

def calculate(strech_size):
    moved_galaxies = []
    for galaxy in galaxies:
        moved_galaxy = list(copy.deepcopy(galaxy))
        for empty_row in empty_rows:
            if empty_row < galaxy[1]:
                moved_galaxy[1] += strech_size - 1

        for empty_column in empty_columns:
            if empty_column < galaxy[0]:
                moved_galaxy[0] += strech_size - 1

        moved_galaxies.append(tuple(moved_galaxy))

    result = 0
    pairs = 0
    for i, galaxy in enumerate(moved_galaxies):
        for j, to_galaxy in enumerate(moved_galaxies):
            if i < j:
                distance = abs(galaxy[0] - to_galaxy[0]) + abs(galaxy[1] - to_galaxy[1])
                result += distance
                pairs += 1
    return result



if __name__ == "__main__":
    space_map = []
    galaxies = []
    with open("./day_11/input.txt", 'r') as file:
        for y, line in enumerate(file):
            row = []
            for x, letter in enumerate(line.strip()):
                row.append(letter)
                if letter == '#':
                    galaxies.append((x, y))
            space_map.append(row)

    galaxies_indexes = [x[0] for x in galaxies]
    empty_columns = [i for i, x in enumerate(range(len(space_map))) if x not in galaxies_indexes]

    galaxies_values = [x[1] for x in galaxies]
    empty_rows = [i for i, x in enumerate(range(len(space_map[0]))) if x not in galaxies_values]


    print("---Part One---")
    print(calculate(2))

    print("---Part Two---")
    print(calculate(1000000))

