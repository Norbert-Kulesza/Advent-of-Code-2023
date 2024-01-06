from collections import Counter
from functools import cmp_to_key

with open("7ainput.txt") as f:
    def deterime_type(hand):
        counter = Counter(hand)
        
        if 5 in counter.values():
            return 7
        elif 4 in counter.values():
            return 6
        elif 3 in counter.values() and 2 in counter.values():
            return 5
        elif 3 in counter.values():
            return 4
        elif list(counter.values()).count(2) == 2:
            return 3
        elif 2 in counter.values():
            return 2
        else:
            return 1
        
    card_values = {
        "T": 10,
        "J": 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }

    def get_value(card):
        if card.isdigit():
            return int(card)
        else:
            return card_values[card]
        
    def compare(hand_bid1, hand_bid2):
        hand1 = hand_bid1[0]
        hand2 = hand_bid2[0]
        
        if deterime_type(hand1) == deterime_type(hand2):
            for card1, card2 in zip(hand1, hand2):
                if get_value(card1) != get_value(card2):
                    return get_value(card1) - get_value(card2)
            else:
                return 0
        else:
            return deterime_type(hand1) - deterime_type(hand2)
       
    hands = [line.strip().split() for lines in f for line in lines.split("\n\n")]
    ordered_hands = sorted(hands, key=cmp_to_key(compare))

    total = 0
    for i, (hand, bid) in enumerate(ordered_hands):
        total += (i + 1) * int(bid)

    print(total)
    