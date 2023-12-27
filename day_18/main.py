import copy

def part_one(data):
    current_position = [0, 0]
    positions = [copy.deepcopy(current_position)]

    length = 0
    for d in data:
        match d[0]:
            case "U":
                current_position[1] -= int(d[1])
            case "D":
                current_position[1] += int(d[1])
            case "R":
                current_position[0] += int(d[1])
            case "L":
                current_position[0] -= int(d[1])
        length += int(d[1])
        positions.append(copy.deepcopy(current_position))

    # Pick's theorem
    shoelace = shoelace_formula(positions)
    i = shoelace - (length // 2) + 1

    return i + length  # Inside squares + outside

def shoelace_formula(polygonBoundary):
    nbCoordinates = len(polygonBoundary)
    nbSegment = nbCoordinates - 1

    result = 0
    for i in range(nbSegment):
        result += (polygonBoundary[i + 1][0] - polygonBoundary[i][0]) * (polygonBoundary[i + 1][1] + polygonBoundary[i][1])

    return abs(result // 2)

def part_two(data):
    current_position = [0, 0]
    positions = [copy.deepcopy(current_position)]

    length = 0

    for d in data:
        hex_val = d[2][1:]
        n = int(hex_val[:-1], 16)
        match "RDLU"[int(hex_val[-1])]:
            case "U":
                current_position[1] -= n
            case "D":
                current_position[1] += n
            case "R":
                current_position[0] += n
            case "L":
                current_position[0] -= n
        positions.append(copy.deepcopy(current_position))
        length += n

    # Pick's theorem
    shoelace = shoelace_formula(positions)
    i = shoelace - (length // 2) + 1

    return i + length # Inside squares + outside








if __name__ == "__main__":

    data = []
    with open("./day_18/input.txt", 'r') as file:
        for line in file:
            info = line.split()
            info[2] = info[2].replace("(", "").replace(")", "")
            data.append(info)

    print("---Part One---")
    print(part_one(data))

    print("---Part Two---")
    print(part_two(data))
