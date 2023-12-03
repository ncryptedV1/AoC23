from operator import mul
from functools import reduce

with open("in2.txt", "r") as file:
    input = file.readlines()
    res = 0
    for line in input:
        game_id, cube_sets = line.split(":")
        game_id = int(game_id[5:])
        max_counts = {"red": 0, "green": 0, "blue": 0}
        for cube_set in cube_sets.split(";"):
            for cube_count in cube_set.split(","):
                count, cube_type = cube_count.strip().split(" ")
                count = int(count)
                max_counts[cube_type] = max(max_counts[cube_type], count)
        res += reduce(mul, max_counts.values(), 1)

    print(res)
