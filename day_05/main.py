# I normally don't like comments, but here they are needed lol

class Function:
    def __init__(self, maps):
        map_lines = maps.split('\n')[1:]
        self.tuples: list[list[int]] = [[int(x) for x in line.split()] for line in map_lines]

    def transform(self, input):
        for (dst, src, sz) in self.tuples:
            if src <= input < src + sz:
                return input + dst - src
        return input

    # [start, end) ranges
    def transform_range(self, input_range):
        transformed_ranges = []

        for (dest, source, range_size) in self.tuples:
            source_end = source + range_size
            not_changed_ranges = []
            while input_range:
                # Eatch range can be splitted into start, middle, end

                # Start and end are not changed by transformation,
                # but maybe other transformations in funtion will change it, so we readd it

                # Middle is changed by this transformation and others WON'T CHANGE IT

                (start, end) = input_range.pop()

                before = (start, min(end, source))
                middle = (max(start, source), min(source_end, end))
                after = (max(source_end, start), end)

                # If before/after are NOT empty
                if before[1] > before[0]:
                    not_changed_ranges.append(before)
                if after[1] > after[0]:
                    not_changed_ranges.append(after)

                # Calculate transformation for middle
                if middle[1] > middle[0]:
                    transformed_ranges.append((middle[0] - source + dest, middle[1] - source + dest))

            input_range = not_changed_ranges
        return transformed_ranges + input_range



def part_one(seeds, functions) -> int:
    results = []
    for seed in seeds:
        for function in functions:
            seed = function.transform(seed)
        results.append(seed)
    return min(results)

if __name__ == "__main__":
    with open("./day_05/input.txt", 'r') as file:
        file = file.read()

    lines = file.split('\n')
    transformers = file.split('\n\n')

    seeds, *maps = transformers
    seeds = [int(x) for x in seeds.split(':')[1].split()]

    functions = [Function(map) for map in maps]

    print("---Part One---")
    print(part_one(seeds, functions))

    print("---Part Two---")
    result = []
    pairs = list(zip(seeds[::2], seeds[1::2]))
    for start, size in pairs:
        function_range = [(start, start + size)]
        for function in functions:
            function_range = function.transform_range(function_range)
        result.append(min(function_range)[0])
    print(min(result))
