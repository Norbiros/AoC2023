from typing import List

text_to_digits = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}


def get_first_number_from_left(text: str) -> int:
    for char in text:
        if char.isdigit():
            return int(char)


def get_numbers(text: str) -> int:
    first_number = get_first_number_from_left(text)
    second_number = get_first_number_from_left(text[::-1])
    return int(f"{first_number}{second_number}")


def part_one(lines: List[str]) -> int:
    result = 0
    for line in lines:
        result += get_numbers(line)
    return result


def parse_text(input_text: str) -> str:
    result = ""
    remaining_text = input_text

    # Interestingly "oneight" should be "18" not "1ight"
    while remaining_text:
        for text_number, digit in text_to_digits.items():
            if remaining_text.startswith(text_number):
                result += digit
                break
        result += remaining_text[0]
        remaining_text = remaining_text[1:]

    for text_number in text_to_digits:
        result = result.replace(text_number, "")
    return result


def part_two(lines: List[str]) -> int:
    fixed_lines = []
    for line in lines:
        fixed_lines.append(parse_text(line))
    return part_one(fixed_lines)


if __name__ == "__main__":
    with open("./day_01/input.txt", 'r') as file:
        input_lines = [line.strip() for line in file]

    print("---Part One---")
    print(part_one(input_lines))

    print("---Part Two---")
    print(part_two(input_lines))
