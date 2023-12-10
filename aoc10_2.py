def coord_to_id(x, y, width):
    return y * width + x


def id_to_coord(id, width):
    y = id // width
    x = id - y * width
    return (x, y)


def coord_move(coord, dir, width, height):
    if dir == "U":
        if coord // width == 0:
            return None
        return coord - width
    elif dir == "D":
        if coord // width == height - 1:
            return None
        return coord + width
    elif dir == "L":
        if coord == 0:
            return None
        return coord - 1
    elif dir == "R":
        if coord == width - 1:
            return None
        return coord + 1


with open("in10.txt", "r") as file:
    pipe_map = [line.strip() for line in file.readlines()]
    width = len(pipe_map[0])
    height = len(pipe_map)

    graph = {}
    pipes = {}
    s_id = None
    for y, row in enumerate(pipe_map):
        for x, pipe in enumerate(row):
            if pipe == ".":
                continue
            cur_id = coord_to_id(x, y, width)
            if pipe == "|":
                dirs = ("U", "D")
            elif pipe == "-":
                dirs = ("L", "R")
            elif pipe == "F":
                dirs = ("D", "R")
            elif pipe == "7":
                dirs = ("L", "D")
            elif pipe == "J":
                dirs = ("L", "U")
            elif pipe == "L":
                dirs = ("U", "R")
            elif pipe == "S":
                s_id = cur_id
                continue
            else:
                print(f"Found unknown tile: {pipe} at ({x}, {y})")
            for neighbor_id in [coord_move(cur_id, dir, width, height) for dir in dirs]:
                if not cur_id in graph:
                    graph[cur_id] = []
                graph[cur_id].append(neighbor_id)
            pipes[cur_id] = pipe

    # now we want to figure out which tiles belong to the loop
    loop_tiles = set()
    # retrieve neighbors of S
    s_connecting_neighbors = []
    for dir in ("U", "D", "L", "R"):
        neighbor_id = coord_move(s_id, dir, width, height)
        if neighbor_id in graph and s_id in graph[neighbor_id]:
            s_connecting_neighbors.append((dir, neighbor_id))
    if len(s_connecting_neighbors) != 2:
        print("Not exactly two connecting neighbors! This is bad...")

    # traverse along neighbors as long as they don't meet
    prev_ids = [s_id, s_id]
    cur_ids = [s_connecting_neighbors[x][1] for x in range(2)]
    loop_tiles.update(cur_ids)
    # as long as the two traversal chains don't meet
    while cur_ids[0] != cur_ids[1]:
        next_ids = [
            list(filter(lambda x: x != prev_id, graph[cur_id]))[0]
            for prev_id, cur_id in zip(prev_ids, cur_ids)
        ]
        loop_tiles.update(next_ids)
        if next_ids[0] == cur_ids[1] and next_ids[1] == cur_ids[0]:
            # also break if the chains pass each other in a single step
            break
        prev_ids = cur_ids
        cur_ids = next_ids

    # also add S to the loop tiles
    loop_tiles.add(s_id)
    s_dirs = (s_connecting_neighbors[0][0], s_connecting_neighbors[1][0])
    s_dir = None
    if all(x in s_dirs for x in ("D", "R")):
        s_dir = 'F'
    elif all(x in s_dirs for x in ("L", "D")):
        s_dir = '7'
    elif all(x in s_dirs for x in ("L", "U")):
        s_dir = 'J'
    elif all(x in s_dirs for x in ("U", "R")):
        s_dir = 'L'
    pipes[s_id] = s_dir

    # iterate over every row
    is_corner_tile = lambda x: x in ("F", "7", "J", "L")
    is_up_corner = lambda x: x in ("L", "J")
    res = 0
    for y, row in enumerate(pipe_map):
        in_graph = False
        pending_tiles_in_graph = 0
        starting_corner_up = None
        precise_cache = []
        for x, pipe in enumerate(row):
            cur_id = coord_to_id(x, y, width)
            # for every pipe in the loop
            if cur_id in loop_tiles:
                pipe_type = pipes[cur_id]
                # check if inside/outside graph has to be switched
                switch_in_graph = False
                if pipe_type == '|':
                    # always switch on vertical pipe
                    switch_in_graph = True
                elif is_corner_tile(pipe_type):
                    cur_is_up_corner = is_up_corner(pipe_type)
                    if starting_corner_up == None:
                        # corner sequence starts
                        starting_corner_up = cur_is_up_corner
                    else:
                        # only switch in/outside graph when start and end corner go in different directions
                        switch_in_graph = starting_corner_up != cur_is_up_corner
                        starting_corner_up = None
                if not switch_in_graph:
                    continue
                
                if in_graph:
                    # when leaving the loop, add the cached nr of tiles to the final result
                    res += pending_tiles_in_graph
                    for precise_cache_id in precise_cache:
                        print(
                            f"{precise_cache_id} -> {id_to_coord(precise_cache_id, width)}"
                        )
                in_graph = not in_graph
                pending_tiles_in_graph = 0
                precise_cache = []
            elif in_graph:
                # when we're inside of the loop, increment the nr of tiles
                pending_tiles_in_graph += 1
                precise_cache.append(cur_id)
    print(res)
