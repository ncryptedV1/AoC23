def check_horizontal_mirror(card, y):
    # check for reflection with mirror between y and y+1
    rows_to_check = min(y + 1, len(card) - y - 1)
    for check_offset in range(1, rows_to_check + 1):
        if card[y - check_offset + 1] != card[y + check_offset]:
            return False
    return True


def check_all_horizontal_mirrors(card):
    for y in range(len(card) - 1):
        if check_horizontal_mirror(card, y):
            return y
    return None


with open("in13.txt", "r") as file:
    # load all maps as strings
    cards = []
    line_cache = []
    for line in file.readlines():
        line = line.strip()
        if line != "":
            line_cache.append(line)
        else:
            cards.append(line_cache)
            line_cache = []
    if len(line_cache) != 0:
        cards.append(line_cache)
        line_cache = []

    res = 0
    for card in cards:
        # check for horizontal mirror match
        horizontal_found = check_all_horizontal_mirrors(card)
        if horizontal_found is not None:
            res += 100 * (horizontal_found + 1)
        else:
            # use zip(*grid) to transpose the card (rotate by 90 degrees)
            transposed_card = list(zip(*card[::-1]))
            rotated_card = [''.join(row) for row in transposed_card]
            # check for horizontal mirror match on transposed card (equivalent to vertical checking)
            vertical_found = check_all_horizontal_mirrors(rotated_card)
            if vertical_found is not None:
                res += vertical_found + 1
    print(res)
