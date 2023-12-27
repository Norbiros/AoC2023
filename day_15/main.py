import copy
from collections import defaultdict
import re


def hash(text):
    current_value = 0
    for letter in text:
        current_value += ord(letter)
        current_value *= 17
        current_value = current_value % 256
    return current_value


def part_one(data):
    result = 0
    for d in data:
        result += hash(d)
    return result


def part_two(data):
    boxes = defaultdict(lambda: [])
    for d in data:
        split = re.split(r"-|=", d)
        d_hash = hash(split[0])
        if "=" in d:
            appended = False
            for i in range(len(boxes[d_hash])):
                check_box = boxes[d_hash][i]
                if check_box.startswith(split[0]):
                    boxes[d_hash][i] = d
                    appended = True
                    break

            if not appended:
                boxes[d_hash].append(d)
        elif "-" in d:
            new_list = copy.deepcopy(boxes[d_hash])
            for i in range(len(boxes[d_hash])):
                check_box = boxes[d_hash][i]
                if check_box.startswith(split[0]):
                    new_list.remove(check_box)
            boxes[d_hash] = new_list

    result = 0
    for box_id, box in boxes.items():
        for i, lens in enumerate(box):
            focal = int(lens.split("=")[1])
            result += int(box_id + 1) * (i + 1) * focal

    return result


if __name__ == "__main__":
    with open("./day_15/input.txt", 'r') as file:
        data = ''.join(file.readlines()).split(",")

    print("---Part One---")
    print(part_one(data))

    print("---Part Two---")
    print(part_two(data))
