from tqdm import tqdm


def make_decision(remaining_states, cur_damaged_seq_len, remaining_damaged_seqs):
    if len(remaining_states) == 0:
        if len(remaining_damaged_seqs) == 0 and cur_damaged_seq_len == 0:
            return 1
        elif len(remaining_damaged_seqs) == 1 and remaining_damaged_seqs[0] == cur_damaged_seq_len:
            return 1
        else:
            return 0
    if cur_damaged_seq_len > 0 and len(remaining_damaged_seqs) == 0:
        return 0

    cur_state = remaining_states[0]
    if len(remaining_damaged_seqs) != 0 and cur_damaged_seq_len > remaining_damaged_seqs[0]:
        return 0

    if cur_state == -1:
        return make_decision(
            [0] + remaining_states[1:], cur_damaged_seq_len, remaining_damaged_seqs
        ) + make_decision(
            [1] + remaining_states[1:], cur_damaged_seq_len, remaining_damaged_seqs
        )
    elif cur_state == 0:
        if cur_damaged_seq_len != 0:
            if cur_damaged_seq_len == remaining_damaged_seqs[0]:
                return make_decision(remaining_states[1:], 0, remaining_damaged_seqs[1:])
            else:
                return 0
        else:
            return make_decision(remaining_states[1:], 0, remaining_damaged_seqs)
    elif cur_state == 1:
        return make_decision(
            remaining_states[1:], cur_damaged_seq_len + 1, remaining_damaged_seqs
        )
    print("meh")

with open("in12.txt", "r") as file:
    res = 0
    for line in tqdm(file.readlines()):
        line_state, line_nrs = line.strip().split(" ")
        line_state = "?".join([line_state] * 5)
        line_nrs = ",".join([line_nrs] * 5)
        damaged_nrs = [int(x) for x in line_nrs.split(",")]
        unknown_idxs = []
        state_list = []  # 0 - operational, 1 - damaged
        for idx, char in enumerate(line_state):
            if char == ".":
                state_list.append(0)
            elif char == "#":
                state_list.append(1)
            elif char == "?":
                unknown_idxs.append(idx)
                state_list.append(-1)

        part_res = make_decision(state_list, 0, damaged_nrs)
        res += part_res
    print(res)
