nrs = []
gears = []

with open("in3.txt", "r") as file:
    for y, line in enumerate(file.readlines()):
        nr_start = None
        cur_nr = ""
        for x, char in enumerate(line.strip()):
            if char == ".":
                continue
            elif char.isdigit():
                if nr_start == None:
                    nr_start = x
                cur_nr += char
            elif char == "*":
                gears.append((x, y))

            # lookahead if cur nr sequence is gonna end
            if x != len(line) and nr_start != None and not line[x + 1].isdigit():
                nrs.append((nr_start, y, int(cur_nr)))
                nr_start = None
                cur_nr = ""

    res = 0
    for gear_x, gear_y in gears:
        gear_nrs = []
        for x, y, nr in nrs:
            total_len = len(str(nr))
            min_x = x - 1
            min_y = y - 1
            max_x = x + total_len
            max_y = y + 1
            if (
                min_x <= gear_x
                and gear_x <= max_x
                and min_y <= gear_y
                and gear_y <= max_y
            ):
                gear_nrs.append(nr)
        if len(gear_nrs) == 2:
            res += gear_nrs[0] * gear_nrs[1]
    print(res)
