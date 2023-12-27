import heapq


def part_one():
    moves_to_do = [(0, 0, 0, -1, -1)]
    finished_moves = {}
    while moves_to_do:
        dist, r, c, direction, in_direction = heapq.heappop(moves_to_do)
        if (r, c, direction, in_direction) in finished_moves:
            continue

        finished_moves[(r, c, direction, in_direction)] = dist
        for i, (dr, dc) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
            rr = r + dr
            cc = c + dc
            new_direction = i
            new_in_direction = (1 if new_direction != direction else in_direction + 1)

            isnt_reverse = ((new_direction + 2) % 4 != direction)

            isvalid = (new_in_direction <= 3)

            if 0 <= rr < width and 0 <= cc < height and isnt_reverse and isvalid:
                cost = int(path_map[rr][cc])
                heapq.heappush(moves_to_do, (dist + cost, rr, cc, new_direction, new_in_direction))

    ans = 1e9
    for (r, c, direction, in_direction), v in finished_moves.items():
        if r == width - 1 and c == height - 1:
            ans = min(ans, v)
    return ans

if __name__ == "__main__":
    with open("./day_17/input.txt", 'r') as file:
        path_map = [[c for c in row.strip()] for row in file.readlines()]

    width = len(path_map)
    height = len(path_map[0])

    print("---Part One---")
    print(part_one())

    # I solved part two on my phone and I can't find it rn and i don't want to rewrite it!
