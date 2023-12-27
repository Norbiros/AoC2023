import copy
from collections import deque


def parse_workflow(name, part, workflows):
    workflow = workflows[name]
    for step in workflow:
        if ":" in step:
            check, next_step = step.split(":")

            for symbol, val in part.items():
                check = check.replace(symbol, str(val))
            result = eval(check)
            if result:
                if next_step == "A":
                    return True
                elif next_step == "R":
                    return False
                else:
                    return parse_workflow(next_step, part, workflows)
        else:
            if step == "A":
                return True
            elif step == "R":
                return False
            else:
                return parse_workflow(step, part, workflows)


def part_one(workflows, parts):
    result = 0
    for part in parts:
        is_accepted = parse_workflow("in", part, workflows)
        if is_accepted:
            result += sum(part.values())

    return result


def new_range(operator, value, cords):
    min_range, max_range = cords
    if operator == '>':
        min_range = max(min_range, value + 1)
    elif operator == '<':
        max_range = min(max_range, value - 1)
    elif operator == '>=':
        min_range = max(min_range, value)
    elif operator == '<=':
        max_range = min(max_range, value)
    else:
        assert False
    return min_range, max_range

def new_ranges(variable, operator, value, cords_x, cords_m, cords_a, cords_s):
    if variable == 'x':
        cords_x = new_range(operator, value, cords_x)
    elif variable == 'm':
        cords_m = new_range(operator, value, cords_m)
    elif variable == 'a':
        cords_a = new_range(operator, value, cords_a)
    elif variable == 's':
        cords_s = new_range(operator, value, cords_s)

    return cords_x, cords_m, cords_a, cords_s


def parse_workflow_range(state, ranges, workflows, i):
    # print(" "*i + state + " " + str(ranges))
    global part_two_ans

    cords_x, cords_m, cords_a, cords_s = ranges
    if cords_x[0] > cords_x[1] or cords_m[0] > cords_m[1] or cords_a[0] > cords_a[1] or cords_s[0] > cords_s[1]:
        return

    if state == "A":
        # print(f"{(cords_x)} {(cords_m)} {(cords_a)} {(cords_s)}")
        answer =  (cords_x[1] - cords_x[0] + 1) * (cords_m[1] - cords_m[0] + 1) * (
                    cords_a[1] - cords_a[0] + 1) * (cords_s[1] - cords_s[0] + 1)
        # print(" "*i + str(answer))
        part_two_ans +=answer
        return
    elif state == "R":
        return

    workflow = workflows[state]
    # print(workflow)
    for step in workflow:
        if ":" in step:
            condition, res = step.split(':')
            variable = condition[0]
            operator = condition[1]
            n = int(condition[2:])

            # print( "Info: " + str(variable) + " " + str(operator) + " " + str(n) + " " + str(state))
            # print("Previous: " + str((cords_x, cords_m, cords_a, cords_s)))
            # print("Next: " + str(new_ranges(variable, operator, n, cords_x, cords_m, cords_a, cords_s)))
            parse_workflow_range(res, new_ranges(variable, operator, n, ranges[0], ranges[1], ranges[2], ranges[3]), workflows, i + 1)
            ranges = new_ranges(variable, '<=' if operator == '>' else '>=', n, ranges[0], ranges[1], ranges[2], ranges[3])

        else:
            parse_workflow_range(step, ranges, workflows, i + 1)


def part_two(workflows, parts):
    ranges = ((1, 4000), (1, 4000), (1, 4000), (1, 4000))

    parse_workflow_range("in", ranges, workflows, 0)

    return part_two_ans


if __name__ == "__main__":

    with open("./day_19/input.txt", 'r') as file:
        file_lines = file.read().strip()
        workflows_input, parts_input = file_lines.split("\n\n")
        workflows_input = workflows_input.strip().splitlines()
        parts_input = parts_input.strip().splitlines()

    parts = []
    for part_input in parts_input:
        part_input = part_input.strip('{}')

        pairs = part_input.split(',')
        data = {}
        for pair in pairs:
            key, value = pair.split('=')
            data[key.strip()] = int(value.strip())
        parts.append(data)

    workflows = {}
    for workflow_input in workflows_input:
        name, workflow_input = workflow_input.split("{")

        workflow_input = workflow_input.strip('}')

        pairs = workflow_input.split(',')
        workflows[name] = pairs

    part_two_ans = 0

    print("---Part One---")
    print(part_one(workflows, parts))

    print("---Part Two---")
    print(part_two(workflows, parts))
