with open("in9.txt", "r") as file:
    res = 0
    for line in file.readlines():
        nrs = [int(x) for x in line.strip().split(' ')]
        diff_history = [nrs]
        while not all(x == 0 for x in diff_history[-1]):
            prev_diffs = diff_history[-1]
            cur_diffs = [prev_diffs[x+1] - prev_diffs[x] for x in range(len(prev_diffs) - 1)]
            diff_history.append(cur_diffs)
        bw_extrapolated = 0
        for diffs in diff_history[-1::-1]:
            bw_extrapolated = diffs[0] - bw_extrapolated
        res += bw_extrapolated
    print(res)