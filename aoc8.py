with open("in8.txt", "r") as file:
    instructions = file.readline().strip()
    file.readline()

    nodes = {}
    for line in file.readlines():
        start, ends = [x.strip() for x in line.split('=')]
        end1, end2 = [x.strip() for x in ends[1:-1].split(',')]
        nodes[start] = (end1, end2)
    
    steps = 0
    cur_pos = 'AAA'
    while instruction := instructions[steps % len(instructions)]:
        if instruction == 'L':
            cur_pos = nodes[cur_pos][0]
        else:
            cur_pos = nodes[cur_pos][1]
        steps += 1

        if cur_pos == 'ZZZ':
            break
    print(steps)