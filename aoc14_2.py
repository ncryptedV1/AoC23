from tqdm import tqdm
from collections import Counter

def calc_load_on_north(card):
    load = 0
    for y, row in enumerate(card[::-1]):
        for char in row:
            if char == 'O':
                load += y + 1
    return load

with open('in14.txt', 'r') as file:
    card = [line for line in file.readlines()]
    # repeat n cycles
    prev_load = []
    for cycle_nr in range(1_000_000_000):
        # repeat for all four cardinal directions
        for dir in range(4):
            # now we can simulate the falling row by row
            # rotate card clockwise 90 degrees to simulate tilting north (->W->S->E) line-by-line
            card = [''.join(row) for row in list(zip(*card[::-1]))]
            new_card = []
            for row in card:
                new_row = []
                cur_falling = 0
                for idx, char in enumerate(row):
                    if char == 'O':
                        cur_falling += 1
                        new_row.append('.')
                    elif char == '#':
                        for x in range(cur_falling):
                            new_row[-1-x] = 'O'
                        cur_falling = 0
                        new_row.append('#')
                    elif char == '.':
                        new_row.append('.')
                if cur_falling != 0:
                    for x in range(cur_falling):
                        new_row[-1-x] = 'O'
                    cur_falling = 0
                new_card.append(''.join(new_row))
            card = new_card

            # after tilting north check for convergence
            if dir == 3:
                load = calc_load_on_north(card)
                if load == 65:
                    print(cycle_nr)
                else:
                    print(cycle_nr)
                # if len(prev_res) != 0 and res == prev_res[-1]:
                #     print(res)
                prev_load.append(load)
                if len(prev_load) % 10_000 == 0:
                    counts = Counter(prev_load)
                    total_count = len(prev_load)
                    percentages = {number: (count / total_count) * 100 for number, count in counts.items()}
                    for nr, pct in percentages.items():
                        print(f"{nr} - {pct}%")
                    exit()
                    print(prev_load[-10:])
                    prev_load = [prev_load[-1]]

    for x in card:
        print(x)
