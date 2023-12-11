with open("in11.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]
    galaxies = []
    empty_rows = set()
    empty_cols = set()
    # collect empty rows
    for row_idx, row in enumerate(lines):
        if all(x == '.' for x in row):
            empty_rows.add(row_idx)
            continue
    # collect empty cols
    for col_idx in range(len(lines[0])):
        if all(row[col_idx] == '.' for row in lines):
            empty_cols.add(col_idx)
    
    # collect galaxies while integrating row/col doubling
    cur_y_off = 0
    for row_idx, row in enumerate(lines):
        if row_idx in empty_rows:
            cur_y_off += 999_999
            continue

        cur_x_off = 0
        for col_idx, char in enumerate(row):
            if col_idx in empty_cols:
                cur_x_off += 999_999
                continue
            if char != '#':
                continue
            galaxies.append((col_idx + cur_x_off, row_idx + cur_y_off))
    
    # calculate distances between all galaxy pairs
    res = 0
    for g_idx1 in range(len(galaxies)):
        g1_x, g1_y = galaxies[g_idx1]
        for g_idx2 in range(g_idx1 + 1, len(galaxies)):
            g2_x, g2_y = galaxies[g_idx2]
            res += abs(g1_x - g2_x) + abs(g1_y - g2_y)
    print(res)
    