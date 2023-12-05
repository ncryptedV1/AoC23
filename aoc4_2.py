import re

with open("in4.txt", "r") as file:
    lines = file.readlines()
    res = 0
    instance_counts = {x: 1 for x in range(len(lines))}
    for idx, line in enumerate(lines):
        winning_nrs, nrs = [
            set(int(y) for y in re.sub(r'\s+', ' ', x.strip()).split(' ')) for x in line.split(":")[1].split("|")
        ]
        match_count = 0
        for nr in nrs:
            if nr in winning_nrs:
                match_count += 1
        for copy_idx_off in range(1, match_count + 1):
            copy_idx = idx+copy_idx_off
            if copy_idx >= len(lines):
                continue
            instance_counts[copy_idx] += instance_counts[idx]
    print(sum(instance_counts.values()))
