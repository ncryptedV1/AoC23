from tqdm import tqdm

def get_sequence_lens(state):
    sequence_lens = []
    cur_len = 0
    for x in state:
        if x == 1:
            cur_len += 1
        elif cur_len != 0:
            sequence_lens.append(cur_len)
            cur_len = 0
    if cur_len != 0:
        sequence_lens.append(cur_len)
    return sequence_lens

with open('in12.txt', 'r') as file:
    res = 0
    for line in tqdm(file.readlines()):
        line_state, line_nrs = line.strip().split(' ')
        damaged_nrs = [int(x) for x in line_nrs.split(',')]
        unknown_idxs = []
        state_list = []  # 0 - operational, 1 - damaged
        for idx, char in enumerate(line_state):
            if char == '.':
                state_list.append(0)
            elif char == '#':
                state_list.append(1)
            elif char == '?':
                unknown_idxs.append(idx)
                state_list.append(-1)
        
        # simulate all possible decisions
        nr_decisions = len(unknown_idxs)
        for dec_coded_decisions in range(2**nr_decisions):
            decision_bit_str = f'{{0:0{nr_decisions}b}}'.format(dec_coded_decisions)
            cur_decisions = state_list.copy()
            for idx, decision in enumerate(decision_bit_str):
                cur_decisions[unknown_idxs[idx]] = int(decision)
            if damaged_nrs == get_sequence_lens(cur_decisions):
                res += 1
    print(res)
