import re

with open("in5.txt", "r") as file:
    seeds = [int(x) for x in file.readline().split(':')[1].strip().split(' ')]

    conv_mode = False
    conv_map = {x: x for x in seeds}
    while line := file.readline():
        is_val_line = line[0].isdigit()
        if not conv_mode and is_val_line:
                conv_mode = True
        if conv_mode:
            if is_val_line:
                dest, source, range_val = [int(x) for x in line.strip().split(' ')]
                for cur_id in conv_map.keys():
                    if cur_id < source  or  cur_id > source + range_val - 1:
                        continue
                    conv_map[cur_id] = cur_id - source + dest
            else:
                 conv_map = {x: x for x in conv_map.values()}
                 conv_mode = False
    print(min(conv_map.values()))
            
            
