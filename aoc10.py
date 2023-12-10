def coord_to_id(x, y, width):
    return y * width + x

def coord_move(coord, dir, width, height):
    if dir == 'U':
        if coord // width == 0:
            return None
        return coord - width
    elif dir == 'D':
        if coord // width == height - 1:
            return None
        return coord + width
    elif dir == 'L':
        if coord == 0:
            return None
        return coord - 1
    elif dir == 'R':
        if coord == width - 1:
            return None
        return coord + 1


with open("in10.txt", "r") as file:
    pipe_map = [line.strip() for line in file.readlines()]
    width = len(pipe_map[0])
    height = len(pipe_map)

    graph = {}
    s_id = None
    for y, row in enumerate(pipe_map):
        for x, pipe in enumerate(row):
            if pipe == '.':
                continue
            cur_id = coord_to_id(x, y, width)
            if pipe == '|':
                dirs = ('U', 'D')
            elif pipe == '-':
                dirs = ('L', 'R')
            elif pipe == 'F':
                dirs = ('D', 'R')
            elif pipe == '7':
                dirs = ('L', 'D')
            elif pipe == 'J':
                dirs = ('L', 'U')
            elif pipe == 'L':
                dirs = ('U', 'R')
            elif pipe == 'S':
                s_id = cur_id
                continue
            for neighbor_id in [coord_move(cur_id, dir, width, height) for dir in dirs]:
                if not cur_id in graph:
                    graph[cur_id] = []
                graph[cur_id].append(neighbor_id)
    # retrieve neighbors of S
    s_connecting_neighbors = []
    for dir in ('U', 'D', 'L', 'R'):
        neighbor_id = coord_move(s_id, dir, width, height)
        if neighbor_id in graph and s_id in graph[neighbor_id]:
            s_connecting_neighbors.append((dir, neighbor_id))
    if len(s_connecting_neighbors) != 2:
        print("Not exactly two connecting neighbors! This is bad...")

    # traverse along neighbors as long as they don't meet
    steps = 1
    prev_ids = [s_id, s_id]
    cur_ids = [s_connecting_neighbors[x][1] for x in range(2)]
    # as long as the two traversal chains don't meet
    while cur_ids[0] != cur_ids[1]:
        next_ids = [list(filter(lambda x: x != prev_id, graph[cur_id]))[0] for prev_id, cur_id in zip(prev_ids, cur_ids)]
        if next_ids[0] == cur_ids[1] and next_ids[1] == cur_ids[0]:
            # also break if the chains pass each other in a single step
            break
        prev_ids = cur_ids
        cur_ids = next_ids
        steps += 1
    print(steps)