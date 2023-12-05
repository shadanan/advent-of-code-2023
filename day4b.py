#!/usr/bin/env python3

with open("input4.txt", "r") as fp:
    lines = fp.read().strip().splitlines()


def get_intersection_len(line: str) -> set:
    _, numbers = line.split(": ")
    left, right = numbers.split(" | ")
    winning_numbers_set = {n for n in left.split()}
    my_numbers_set = {n for n in right.split()}
    intersection = winning_numbers_set.intersection(my_numbers_set)
    return len(intersection)


if __name__ == "__main__":
    # Initialize dict with starting value of 1 for each card id
    cards = {i + 1: 1 for i, _ in enumerate(lines)}

    for i, line in enumerate(lines):
        intersection_len = get_intersection_len(line)
        card_id = i + 1
        # get next winning cards
        for k in range(card_id + 1, card_id + 1 + intersection_len):
            cards[k] += cards[card_id]

    print(sum(cards.values()))
