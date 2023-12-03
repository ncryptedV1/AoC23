nrs = []
symbols = []

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
            else:
                symbols.append((x, y))

            # lookahead if cur nr sequence is gonna end
            if x != len(line) and nr_start != None and not line[x + 1].isdigit():
                nrs.append((nr_start, y, int(cur_nr)))
                nr_start = None
                cur_nr = ""

    res = 0
    for x, y, nr in nrs:
        total_len = len(str(nr))
        min_x = x - 1
        min_y = y - 1
        max_x = x + total_len
        max_y = y + 1
        found = False
        for symbol_x, symbol_y in symbols:
            if (
                min_x <= symbol_x
                and symbol_x <= max_x
                and min_y <= symbol_y
                and symbol_y <= max_y
            ):
                found = True
                break
        if found:
            res += nr
    print(res)
