import copy
import sys
from collections import defaultdict, deque

def part_one(connections):
    # I converted graph to svg, and found information in inkscape:
    # 1st line: mbq -> vgk
    # 2n line: thl -> nmv
    # 3rd line: fzb -> fxr
    #
    # Random node on left side: nvz
    nodes = set()
    end_points = ["mbq", "thl", "fzb"]

    to_check = deque(["nvz"])
    while to_check:
        node = to_check.popleft()
        for connection in connections[node]:
            if connection not in nodes and connection not in end_points:
                to_check.append(connection)
                nodes.add(connection)

    left_nodes = len(nodes) + len(end_points)
    all_nodes = len(connections.keys())
    right_nodes = all_nodes - left_nodes

    return left_nodes * right_nodes


if __name__ == "__main__":
    lines = []
    connections = defaultdict(lambda: [])
    with open("./day_25/input.txt", 'r') as file:
        for line_input in file:
            name, connections_input = line_input.split(": ")
            for connection_input in connections_input.strip().split(" "):
                connections[name].append(connection_input)
                connections[connection_input].append(name)

    print("---Part One---")
    print(part_one(connections))

    print("---Part Two---")
    print("Pushed The Big Red Button!")
