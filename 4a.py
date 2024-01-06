import math

total = 0

with open("4ainput.txt") as f:
    for line in f.readlines():
        winning, regular = line.split("|")
        nr_matches = 0
        winning_cards = set()

        winning_cards_list = list(filter(lambda x: x != "", winning.split(":")[1].split(" ")))
        regular_cards_list = list(filter(lambda x: x != "", regular.strip().split(" ")))

        for winning_card in winning_cards_list:
            winning_cards.add(winning_card)

        for regular_card in regular_cards_list:
            if regular_card in winning_cards:
                nr_matches += 1

        if nr_matches != 0:
            total += int(math.pow(2, nr_matches - 1))
        
print(total)