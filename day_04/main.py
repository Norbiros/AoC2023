from collections import defaultdict
from typing import List


def part_one(lines: List[str]) -> int:
    result = 0
    for line in lines:
        game, cards = line.split(": ")
        winning, yours = cards.split(" | ")
        winning_cards = [int(x) for x in winning.split()]
        yours_cards = [int(x) for x in yours.split()]
        points = 0
        for your_card in yours_cards:
            if your_card in winning_cards:
                if points == 0:
                    points = 1
                else:
                    points *= 2
        result += points

    return result


def part_two(lines: List[str]) -> int:
    copies_amount = defaultdict(lambda: 0)
    for line in lines:
        game, cards = line.split(": ")
        game_id = int(game.replace("Card ", ""))
        copies_amount[game_id] += 1
        winning, yours = cards.split(" | ")
        winning_cards = [int(x) for x in winning.split()]
        yours_cards = [int(x) for x in yours.split()]
        result = 0
        for your_card in yours_cards:
            if your_card in winning_cards:
                result += 1

        for _ in range(copies_amount[game_id]):
            for i in range(result):
                copies_amount[i + game_id + 1] += 1

    return sum(copies_amount.values())


if __name__ == "__main__":
    with open("./day_04/input.txt", 'r') as file:
        input_lines = [line.strip() for line in file]

    print("---Part One---")
    print(part_one(input_lines))

    print("---Part Two---")
    print(part_two(input_lines))
