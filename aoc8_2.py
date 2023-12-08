import math

with open("in8.txt", "r") as file:
    instructions = file.readline().strip()
    file.readline()

    end_nodes = set()
    starting_nodes = []
    nodes = {}
    for line in file.readlines():
        start, ends = [x.strip() for x in line.split('=')]
        end1, end2 = [x.strip() for x in ends[1:-1].split(',')]
        nodes[start] = (end1, end2)
        if start.endswith('A'):
            starting_nodes.append(start)
        if start.endswith('Z'):
            end_nodes.add(start)
    
    steps = 0
    first_finish = {}
    cur_positions = starting_nodes
    while not len(first_finish) == len(cur_positions):
        instruction = 0 if instructions[steps % len(instructions)] == 'L' else 1
        for idx, cur_pos in enumerate(cur_positions):
            if cur_pos in end_nodes:
                if idx not in first_finish:
                    first_finish[idx] = steps
            cur_positions[idx] = nodes[cur_pos][instruction]
        steps += 1
    
    print(math.lcm(*first_finish.values()))
