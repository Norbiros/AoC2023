from collections import Counter


def get_card_type(amounts):
    if sorted(amounts.values()) == [5]:
        return 7
    if sorted(amounts.values()) == [1, 4]:
        return 6
    if sorted(amounts.values()) == [2, 3]:
        return 5
    if sorted(amounts.values()) == [1, 1, 3]:
        return 4
    if sorted(amounts.values()) == [1, 2, 2]:
        return 3
    if sorted(amounts.values()) == [1, 1, 1, 2]:
        return 2
    if sorted(amounts.values()) == [1, 1, 1, 1, 1]:
        return 1


def score_part_one(value):
    order = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    new_text = ''.join([chr(order.index(letter)) for letter in value])

    return get_card_type(Counter(value)), new_text


def part_one(data):
    sorted_data = sorted(data, key=lambda a: score_part_one(a[0]))
    result = 0
    for i, value in enumerate(sorted_data):
        result += (i + 1) * value[1]
    return result


def score_part_two(value):
    order = ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
    hand = ''.join([chr(order.index(letter) + 49) for letter in value])
    hand.replace('J', 'X')  # X is jocker

    amounts = Counter(hand)
    target = list(amounts.keys())[0]
    for k in amounts:
        if k != 'X' and (amounts[k] > amounts[target] or target == 'X'):
            target = k

    if 'X' in amounts and target != 'X':
        amounts[target] += amounts['X']
        del amounts['X']

    return get_card_type(amounts), hand


def part_two(data):
    sorted_data = sorted(data, key=lambda a: score_part_two(a[0]))
    result = 0
    for i, value in enumerate(sorted_data):
        result += (i + 1) * value[1]
    return result


if __name__ == "__main__":
    input_data = []
    with open("./day_07/input.txt", 'r') as file:
        for line in file:
            card, points = line.split()
            input_data.append(tuple([card, int(points)]))

    print("---Part One---")
    print(part_one(input_data))

    print("---Part Two---")
    print(part_two(input_data))
