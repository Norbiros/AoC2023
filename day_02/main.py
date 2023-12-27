from collections import defaultdict
from typing import List


def parse_colors(colors_str: str):
    colors_amount = defaultdict(lambda: 0)
    colors = colors_str.split(", ")
    for color in colors:
        amount, color_name = color.split(" ")
        colors_amount[color_name] += int(amount)

    return colors_amount


def part_one(lines: List[str]) -> int:
    whole_result = 0
    for line in lines:
        colors_min_amount = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        game, result = line.split(": ")
        results = [t.strip() for t in result.split(";")]
        for result in results:
            colors_amount = parse_colors(result)
            for color, color_amount in colors_amount.items():
                if colors_min_amount[color] < color_amount:
                    colors_min_amount[color] = color_amount

        if colors_min_amount["red"] <= 12 and colors_min_amount["green"] <= 13 and colors_min_amount["blue"] <= 14:
            game_id = game.replace("Game ", "")
            whole_result += int(game_id)
    return whole_result


def part_two(lines: List[str]) -> int:
    whole_result = 0
    for line in lines:
        power = 1
        colors_min_amount = {
            "red": 0,
            "green": 0,
            "blue": 0
        }
        game, result = line.split(": ")
        results = [t.strip() for t in result.split(";")]
        for result in results:
            colors_amount = parse_colors(result)
            for color, color_amount in colors_amount.items():
                if colors_min_amount[color] < color_amount:
                    colors_min_amount[color] = color_amount

        for min_color in colors_min_amount.values():
            power *= min_color

        whole_result += power
    return whole_result


if __name__ == "__main__":
    with open("./day_02/input.txt", 'r') as file:
        input_lines = [line.strip() for line in file]

    print("---Part One---")
    print(part_one(input_lines))

    print("---Part Two---")
    print(part_two(input_lines))
