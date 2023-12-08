from collections import defaultdict

def get_best_type(hand: str):
    # count occurence of each card
    char_count = defaultdict(int)
    for char in hand:
        char_count[char] += 1
    counts = sorted(dict(char_count).values(), reverse=True)
    if counts[0] == 5:
        return 7
    elif counts[0] == 4:
        return 6
    elif counts[0] == 3 and counts[1] == 2:
        return 5
    elif counts[0] == 3:
        return 4
    elif counts[0] == 2 and counts[1] == 2:
        return 3
    elif counts[0] == 2:
        return 2
    else:
        return 1

card_ranks = {'2' : 1, '3': 2, '4': 3, '5': 4, '6': 5, '7': 6, '8': 7, '9': 8, 'T': 9, 'J': 10, 'Q': 11, 'K': 12, 'A': 13}
def get_card_ranks(hand: str):
    return [card_ranks[x] for x in hand]

with open('in7.txt', 'r') as file:
    hands = []
    for line in file.readlines():
        line = line.strip()
        hand, bid = line.split(' ') 

        hands.append((get_best_type(hand), get_card_ranks(hand), hand, int(bid)))
    hands = sorted(hands)
    print(hands)
    res = 0
    for idx, (_, _, _, bid) in enumerate(hands):
        res += bid * (idx + 1)
    print(res)
