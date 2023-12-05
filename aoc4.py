import re

with open("in4.txt", "r") as file:
    res = 0
    for line in file.readlines():
        winning_nrs, nrs = [
            set(int(y) for y in re.sub(r'\s+', ' ', x.strip()).split(' ')) for x in line.split(":")[1].split("|")
        ]
        match_nrs = set()
        for nr in nrs:
            if nr in winning_nrs:
                match_nrs.add(nr)
        if len(match_nrs) > 0:
            res += 2 ** (len(match_nrs) - 1)
    print(res)
