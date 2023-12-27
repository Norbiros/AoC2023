import copy
from collections import Counter


class Cuboid:
    def __init__(self, x1, y1, z1, x2, y2, z2, name):
        self.x1, self.y1, self.z1 = x1, y1, z1
        self.x2, self.y2, self.z2 = x2, y2, z2
        self.name = name

    def is_collision(self, other_cuboid):
        x_collision = (self.x1 <= other_cuboid.x2) and (self.x2 >= other_cuboid.x1)
        y_collision = (self.y1 <= other_cuboid.y2) and (self.y2 >= other_cuboid.y1)
        z_collision = (self.z1 <= other_cuboid.z2) and (self.z2 >= other_cuboid.z1)

        return x_collision and y_collision and z_collision

    def __repr__(self):
        return f"Cuboid {self.name} {self.x1} {self.y1} {self.z1} to {self.x2} {self.y2} {self.z2}"


def part_one():
    result = 0
    for supporter, supported_list in collides_list.items():
        if len([x for x in supported_list if items[x] <= 1]) == 0:
            result += 1

    return result


def part_two():
    cache = set()

    def count_nodes_to_remove(graph, val):
        dependencies = {node: set(dependency) for node, dependency in graph.items()}
        removed_nodes = set()

        def remove_node(node):
            removed_nodes.add(node)
            for dependent_node in list(dependencies[node]):
                dependencies[node].remove(dependent_node)
                if not any(dependent_node in deps for deps in dependencies.values()):
                    remove_node(dependent_node)

        remove_node(val)

        return len(removed_nodes)

    result = 0
    for supporter, supported_list in collides_list.items():
        if len([x for x in supported_list if items[x] <= 1]) != 0:
            result += count_nodes_to_remove(copy.deepcopy(collides_list), supporter) - 1
    return result


if __name__ == "__main__":
    positions = []
    with open("./day_22/input.txt", 'r') as file:
        for i, line in enumerate(file):
            positions_text = line.split("~")
            positions.append(
                Cuboid(*[int(x) for x in positions_text[0].split(",")], *[int(x) for x in positions_text[1].split(",")],
                       str(i)))

    sorted_positions = sorted(positions, key=lambda r: min(r.z1, r.z2))
    new_list = copy.deepcopy(sorted_positions)
    collides_list = {x: [] for x in [position.name for position in sorted_positions]}
    for i, sorted_position in enumerate(sorted_positions):
        pos_to_add = copy.deepcopy(sorted_position)
        while True:
            new_position = copy.deepcopy(pos_to_add)
            new_position.z1 -= 1
            new_position.z2 -= 1
            my_down = min(new_position.z1, new_position.z2)

            if my_down < 1:
                break

            collided = False
            for lower_position_id in range(len(sorted_positions)):
                lower_position = new_list[lower_position_id]
                if lower_position.name is not new_position.name and new_position.is_collision(lower_position):
                    collides_list[lower_position.name].append(new_position.name)
                    collided = True

            if collided:
                break
            else:
                pos_to_add = new_position

        new_list[i] = pos_to_add

    all_elements = [element for sublist in collides_list.values() for element in sublist]
    items = Counter(all_elements)

    print("---Part One---")
    print(part_one())

    print("---Part Two---")
    print(part_two())
