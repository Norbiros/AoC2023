def part_one(times, distances):
    result = 1 #Maybe fix
    for i in range(len(times)):
        distance = distances[i]
        time = times[i]
        winning_ways = 0
        for hold_time in range(1, time):
            remaining_time = time - hold_time
            current_distance = remaining_time * hold_time
            if current_distance > distance:
                winning_ways += 1

        result *= winning_ways
    return result

def part_two(time, distance):
    winning_ways = 0
    for hold_time in range(1, time):
        remaining_time = time - hold_time
        current_distance = remaining_time * hold_time
        if current_distance > distance:
            winning_ways += 1
        # if hold_time % 10000 == 0:
            # print(hold_time)

    return winning_ways

if __name__ == "__main__":
    with open("./day_06/input.txt", 'r') as file:
        time_line = file.readline().replace('Time:', '').strip()
        times = [int(x) for x in time_line.split()]

        distance_line = file.readline().replace('Distance:', '').strip()
        distances = [int(x) for x in distance_line.split()]


    print("---Part One---")
    print(part_one(times, distances))

    print("---Part Two---")
    print(part_two(int(time_line.replace(' ', '')), int(distance_line.replace(' ', ''))))