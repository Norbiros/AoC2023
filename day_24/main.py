import copy
import sys
from collections import defaultdict

from z3 import Int, Ints, Solver


class Line:
    # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection#Given_two_line_equations
    def __init__(self, start_cords, velocities):
        self.start_x = start_cords[0]
        self.start_y = start_cords[1]
        self.start_z = start_cords[2]

        self.velocity_x = velocities[0]
        self.velocity_y = velocities[1]
        self.velocity_z = velocities[2]

        # Slopes - https://en.wikipedia.org/wiki/Slope
        self.a = self.velocity_y
        self.b = -self.velocity_x
        self.c = self.velocity_y * self.start_x - self.velocity_x * self.start_y

    def get_interception_point(self, other_line):
        if self.a * other_line.b == other_line.a * self.b:
            return None

        x_intersection = (self.c * other_line.b - other_line.c * self.b) / (
                self.a * other_line.b - other_line.a * self.b)

        y_intersection = (other_line.c * self.a - self.c * other_line.a) / (
                self.a * other_line.b - other_line.a * self.b)

        return x_intersection, y_intersection

    def __repr__(self):
        return f"Line {{ Start {self.start_x} {self.start_y} End {self.velocity_x} {self.velocity_y} }}"


def part_one(lines):
    result = 0
    min_val = 200000000000000
    max_val = 400000000000000
    for index, line in enumerate(lines):
        for other_line in lines[:index]:
            intercept = line.get_interception_point(other_line)
            if intercept is None:
                continue
            x, y = intercept
            if min_val <= x <= max_val and min_val <= y <= max_val:
                # Check if check happens in future
                if (x - line.start_x) * line.velocity_x >= 0 and (y - line.start_y) * line.velocity_y >= 0 and (
                        (x - other_line.start_x) * other_line.velocity_x >= 0 and (
                        y - other_line.start_y) * other_line.velocity_y >= 0):
                    result += 1
    return result

def part_two(lines):
    collision_times = [Int(f"T{i}") for i in range(len(lines))]
    # Rock position
    x, y, z, velocity_x, velocity_y, velocity_z = Ints("x, y, z, velocity_x, velocity_y, velocity_z")

    solver = Solver()
    for i, line in enumerate(lines):
        solver.add(x + velocity_x * collision_times[i] == line.start_x + collision_times[i] * line.velocity_x)
        solver.add(y + velocity_y * collision_times[i] == line.start_y + collision_times[i] * line.velocity_y)
        solver.add(z + velocity_z * collision_times[i] == line.start_z + collision_times[i] * line.velocity_z)

    solver.check()
    model = solver.model()
    return model.eval(x + y + z)

if __name__ == "__main__":
    lines = []
    with open("./day_24/input.txt", 'r') as file:
        for line_input in file:
            start_input, velocity_input = line_input.split(" @ ")
            lines.append(Line([int(x) for x in start_input.split(",")], [int(x) for x in velocity_input.split(",")]))

    print("---Part One---")
    print(part_one(lines))

    print("---Part Two---")
    print(part_two(lines))
