from queue import Queue


def get_next_coords(x, y, dir, width, height):
    if dir == 0 and y > 0:
        # up
        return (x, y - 1)
    elif dir == 1 and y < height - 1:
        # down
        return (x, y + 1)
    elif dir == 2 and x > 0:
        # left
        return (x - 1, y)
    elif dir == 3 and x < width - 1:
        return (x + 1, y)


def get_diverted_dir(dir, field_type):
    regular_mapping = {0: 3, 1: 2, 2: 1, 3: 0}
    back_mapping = {0: 2, 1: 3, 2: 0, 3: 1}
    if field_type == "/":
        return regular_mapping[dir]
    elif field_type == "\\":
        return back_mapping[dir]


def get_split_dir(dir, field_type):
    horizontal_mapping = {0: (2, 3), 1: (2, 3), 2: (2,), 3: (3,)}
    vertical_mapping = {0: (0,), 1: (1,), 2: (0, 1), 3: (0, 1)}
    if field_type == "-":
        return horizontal_mapping[dir]
    elif field_type == "|":
        return vertical_mapping[dir]


with open("in16.txt", "r") as file:
    card = [line.strip() for line in file.readlines()]
    height = len(card)
    width = len(card[0])
    res = 0
    starting_points = [(x, 0, 1) for x in range(width)] + [(0, y, 2) for y in range(height)] + [(x, height-1, 0) for x in range(width)] + [(0, y, 3) for y in range(height)]
    for s_x, s_y, s_dir in starting_points:
        # for each field in each row, create an array of 4 boolean values indicating
        # whether a ray has already passed in a specific direction - up, down, left,
        # right
        dirs_passed = [[[False] * 4 for _ in range(len(line))] for line in card]
        energized = [[False for _ in range(len(line))] for line in card]
        queue = Queue()
        queue.put((s_x, s_y, s_dir))
        while queue.qsize() != 0:
            x, y, dir = queue.get()
            if dirs_passed[y][x][dir] == True:
                continue
            dirs_passed[y][x][dir] = True
            energized[y][x] = True

            field_type = card[y][x]
            if field_type == ".":
                new_coords = get_next_coords(x, y, dir, width, height)
                if new_coords is not None:
                    queue.put((*new_coords, dir))
            elif field_type in ["/", "\\"]:
                new_dir = get_diverted_dir(dir, field_type)
                new_coords = get_next_coords(x, y, new_dir, width, height)
                if new_coords is not None:
                    queue.put((*new_coords, new_dir))
            elif field_type in ["-", "|"]:
                for new_dir in get_split_dir(dir, field_type):
                    new_coords = get_next_coords(x, y, new_dir, width, height)
                    if new_coords is not None:
                        queue.put((*new_coords, new_dir))
        res = max(res, sum([sum(line) for line in energized]))
    print(res)
