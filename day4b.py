#!/usr/bin/env python3

with open("input4.txt", "r") as fp:
    lines = fp.read().strip().splitlines()


def parse_cards(lines: list[str]) -> dict[int, int]:
    cards_mapping = {}
    for line in lines:
        card_str, numbers = line.split(": ")
        card_id = int(card_str.split()[1])
        left, right = numbers.split(" | ")
        winning_numbers_set = {n for n in left.split()}
        my_numbers_set = {n for n in right.split()}
        intersection = winning_numbers_set.intersection(my_numbers_set)
        cards_mapping[card_id] = len(intersection)
    return cards_mapping


if __name__ == "__main__":
    # Initialize dict with starting value of 1 for each card id
    cards_mapping = parse_cards(lines)
    cards = {card_id: 1 for card_id in cards_mapping.keys()}

    # loop through cards in order by key (dict is ordored in Python 3)
    for card_id, intersection_len in cards_mapping.items():
        # get next winning cards for the current card
        for k in range(card_id + 1, card_id + 1 + intersection_len):
            cards[k] += cards[card_id]

    print(sum(cards.values()))
