def map_sequence(input_sequence):
    sequence = []
    for index in range(1, len(input_sequence)):
        sequence.append(input_sequence[index] - input_sequence[index - 1])
    return sequence


def process_sequences(sequences, forward):
    result = 0
    for sequence in sequences:
        converted_sequences = [sequence]
        while any(y != 0 for y in converted_sequences[-1]):
            converted_sequences.append(map_sequence(converted_sequences[-1]))

        for index, converted_sequence in enumerate(reversed(converted_sequences[1:])):
            next_index = len(converted_sequences) - index - 2
            if forward:
                converted_sequences[next_index].append(converted_sequences[next_index][-1] + converted_sequence[-1])
            else:
                converted_sequences[next_index].insert(0, converted_sequences[next_index][0] - converted_sequence[0])

        result += (converted_sequences[0][-1] if forward else converted_sequences[0][0])

    return result


def part_one(sequences):
    return process_sequences(sequences, True)


def part_two(sequences):
    return process_sequences(sequences, False)


if __name__ == "__main__":
    sequences = []
    with open("./day_09/input.txt", 'r') as file:
        for line in file:
            sequences.append([int(x) for x in line.split()])

    print("---Part One---")
    print(part_one(sequences))

    print("---Part Two---")
    print(part_two(sequences))
