def part_one(patterns):
    result = 0
    for pattern in patterns:

        # Calculate columns
        for row_id, row in enumerate(pattern):
            success = True
            for i in range(len(row)):
                if not (0 <= row_id - i < row_id + i + 1 < len(row)):
                    break

                left_column = row[row_id - i]
                right_colum = row[row_id + i + 1]

                if sorted(left_column) != sorted(right_colum):
                    success = False

            if success:
                result += row_id + 1

        for row_id in range(len(pattern[0])):
            success = True
            for i in range(len(pattern[0])):
                if not (0 <= row_id - i < row_id + i + 1 < len(pattern)):
                    break

                left_column = pattern[row_id - i]
                right_colum = pattern[row_id + i + 1]

                if sorted(left_column) != sorted(right_colum):
                    success = False

            if success:
                result += (row_id + 1) * 100
    return result


if __name__ == "__main__":
    patterns = []
    with open("./day_13/input.txt", 'r') as file:
        patterns_text = file.read().split("\n\n")
        for pattern_text in patterns_text:
            pattern_map = pattern_text.split('\n')
            patterns.append([[c for c in row] for row in pattern_map])

    print("---Part One---")
    print(part_one(patterns))

    print("---Part Two---")
    # print(part_two(rows))
