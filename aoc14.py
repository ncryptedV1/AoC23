with open('in14.txt', 'r') as file:
    card = [line for line in file.readlines()]
    # rotate clockwise 90 degrees
    card = [''.join(row) for row in list(zip(*card[::-1]))]
    # now we can simulate the falling row by row
    res = 0
    for row in card:
        cur_falling = 0
        for idx, char in enumerate(row):
            if char == 'O':
                cur_falling += 1
            elif char == '#':
                for x in range(cur_falling):
                    res += idx - x
                cur_falling = 0
        if cur_falling != 0:
            for x in range(cur_falling):
                res += len(row) - x
            cur_falling = 0
    print(res)
