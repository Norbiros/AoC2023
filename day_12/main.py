import copy
from itertools import product


def count_hashes_between_dots(input_str):
    counts = []

    # Find indices of '.' or '?' in the pattern
    dot_indices = [i for i, char in enumerate(input_str) if char in ('.', '?')]

    # Iterate through each pair of '.' or '?' and count '#' in between
    for i in range(1, len(dot_indices)):
        start = dot_indices[i - 1]
        end = dot_indices[i]
        count = input_str[start + 1:end].count('#')
        counts.append(count)

    return list(filter(lambda x: x != 0, counts))


def generate_permutations(pattern):
    replacements = {'?': ['#', '.']}
    pattern_replaced = [replacements.get(char, [char]) for char in pattern]
    permutations = [''.join(p) for p in product(*pattern_replaced)]
    return permutations


def fill_pipes(pipes, sequences, position, current_sequence, current_sequence_length):
    key = (position, current_sequence, current_sequence_length)
    if key in DP:
        return DP[key]

    if position == len(pipes):
        if current_sequence == len(sequences) and current_sequence_length == 0:
            return 1  # Ended with "."
        elif current_sequence == len(sequences) - 1 and sequences[current_sequence] == current_sequence_length:
            return 1  # Finished with "#" and closed block
        return 0

    ans = 0
    for possible_symbol in ['.', '#']:
        if pipes[position] == possible_symbol or pipes[position] == '?':
            if possible_symbol == '.' and current_sequence_length == 0:
                ans += fill_pipes(pipes, sequences, position + 1, current_sequence, 0)  # Adding nothing
            elif possible_symbol == '.' and current_sequence < len(sequences) and sequences[current_sequence] == current_sequence_length: # REMOVE and current_sequence_length > 0
                ans += fill_pipes(pipes, sequences, position + 1, current_sequence + 1, 0)  # Starting new sequence
            elif possible_symbol == '#':
                ans += fill_pipes(pipes, sequences, position + 1, current_sequence, current_sequence_length + 1)  # Continuing sequence
    DP[key] = ans
    return ans


def part_one(rows):
    result = 0
    for row in rows:
        pipes, sequence = row.split()
        sequence = [int(x) for x in sequence.split(",")]

        line_result = 0
        permutations = generate_permutations(pipes)
        for permutation in permutations:
            res = [y for y in [x.count("#") for x in permutation.split(".")] if y != 0]
            if res == sequence:
                line_result += 1
        result += line_result

    return result


def part_two(rows):
    result = 0
    for row in rows:
        pipes, sequence = row.split()
        pipes = "?".join([pipes] * 5)
        sequence = [int(x) for x in sequence.split(",")]*5

        a = fill_pipes(pipes, sequence, 0, 0, 0)
        result += a

    return result


if __name__ == "__main__":
    rows = []
    DP = {}
    with open("./day_12/input.txt", 'r') as file:
        for line in file:
            rows.append(line.strip())

    print("---Part One---")
    print(part_one(rows))

    print("---Part Two---")
    print(part_two(rows))
