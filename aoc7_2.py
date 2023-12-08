from collections import defaultdict


joker_raise_map = {1: 2, 2: 4, 3: 5, 4: 6, 5: 6, 6: 7, 7: 7}


def get_best_type(hand: str):
    # count occurence of each card
    char_count = defaultdict(int)
    for char in hand:
        char_count[char] += 1
    joker_count = 0
    if 'J' in char_count:
        joker_count = char_count['J']
        del char_count['J']
    counts = sorted(dict(char_count).values(), reverse=True)
    best_type = None
    if len(counts) == 0 or counts[0] == 5:
        # if counts is empty, all cards were jokers
        best_type = 7
    elif counts[0] == 4:
        best_type = 6
    elif counts[0] == 3 and len(counts) > 1 and counts[1] == 2:
        best_type = 5
    elif counts[0] == 3:
        best_type = 4
    elif counts[0] == 2 and len(counts) > 1 and counts[1] == 2:
        best_type = 3
    elif counts[0] == 2:
        best_type = 2
    else:
        best_type = 1

    for _ in range(joker_count):
        best_type = joker_raise_map[best_type]
    return best_type


card_ranks = {
    "J": 0,
    "2": 1,
    "3": 2,
    "4": 3,
    "5": 4,
    "6": 5,
    "7": 6,
    "8": 7,
    "9": 8,
    "T": 9,
    "Q": 11,
    "K": 12,
    "A": 13,
}


def get_card_ranks(hand: str):
    return [card_ranks[x] for x in hand]


with open("in7.txt", "r") as file:
    hands = []
    for line in file.readlines():
        line = line.strip()
        hand, bid = line.split(" ")

        hands.append((get_best_type(hand), get_card_ranks(hand), hand, int(bid)))
    hands = sorted(hands)
    print(hands)
    res = 0
    for idx, (_, _, _, bid) in enumerate(hands):
        res += bid * (idx + 1)
    print(res)
