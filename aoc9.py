with open("in9.txt", "r") as file:
    res = 0
    for line in file.readlines():
        nrs = [int(x) for x in line.strip().split(' ')]
        diff_history = [nrs]
        while not all(x == 0 for x in diff_history[-1]):
            prev_diffs = diff_history[-1]
            cur_diffs = [prev_diffs[x+1] - prev_diffs[x] for x in range(len(prev_diffs) - 1)]
            diff_history.append(cur_diffs)
        res += sum(x[-1] for x in diff_history)
    print(res)