from collections import defaultdict

total = 0
card_copies = defaultdict(int)

with open("4ainput.txt") as f:
    for line in f.readlines():
        winning, regular = line.split("|")
        nr_matches = 0
        winning_cards = set()

        card_nr = winning.split(":")[0].split(" ")[-1]
        winning_cards_list = list(filter(lambda x: x != "", winning.split(":")[1].split(" ")))
        regular_cards_list = list(filter(lambda x: x != "", regular.strip().split(" ")))

        card_copies[card_nr] += 1

        for winning_card in winning_cards_list:
            winning_cards.add(winning_card)

        for regular_card in regular_cards_list:
            if regular_card in winning_cards:
                nr_matches += 1

        for i in range(nr_matches):
            card_copies[str(int(card_nr) + i + 1)] += card_copies[card_nr]

        total += card_copies[card_nr]

print(total)