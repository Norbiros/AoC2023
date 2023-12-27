import copy
from collections import deque, defaultdict


def part_one(connection, types, receives):
    memory = {}
    for k, v in receives.items():
        if k == "output":
            continue
        t = types[k]
        if t == "%":
            memory[k] = False
        elif t == "&":
            memory[k] = [False for _ in v]

    high = 0
    low = 0

    moves_to_do = deque([["button,broadcaster,low"]])
    while moves_to_do:
        values = []
        move_to_do = moves_to_do.pop()

        for move_key in move_to_do:
            from_where, move, beam_type = move_key.split(",")
            if move == "output":
                continue
            t = types[move]
            val = connection[move]
            for c in val:
                if t == "broadcaster":
                    values.append(f"{move},{c},low")
                if t == "%":
                    # print(move, memory[move])
                    print(move, beam_type, memory[move])
                    if beam_type == "low":
                        memory[move] = not memory[move]
                        values.append(f"{move},{c},{'high' if memory[move] else 'low'}")
                if t == "&":
                    memory[move][receives[move].index(from_where)] = (beam_type == 'high')
                    # print("lol", sends_to[move].index(c))
                    # print(move, beam_type, f"{move_key}")
                    values.append(f"{move},{c},{'low' if all(memory[move]) else 'high'}")


        if len(values) != 0:
            moves_to_do.append(values)
            for val in values:
                _, _, val_type = val.split(",")
                if val_type == "high":
                    high += 1
                elif val_type == "low":
                    low += 1
        # print(values)
    # print(connection)
    # print(types)
    # print(receives)
    # print(memory)
    return high, low


if __name__ == "__main__":
    modules_connections = {}
    module_types = {}
    module_receives = defaultdict(lambda: [])

    with open("./day_20/input.txt", 'r') as file:
        for line in file:
            module, to = line.split(" -> ")
            module_name = module[1::]
            module_type = module[0]

            if module == "broadcaster":
                module_name = "broadcaster"
                module_type = "broadcaster"

            sends_to = to.strip().split(", ")
            module_types[module_name] = module_type

            modules_connections[module_name] = sends_to
            for destination in sends_to:
                module_receives[destination].append(module_name)


    print("---Part One---")
    print(part_one(modules_connections, module_types, module_receives))

    print("---Part Two---")
    # print(part_two(workflows, parts))
