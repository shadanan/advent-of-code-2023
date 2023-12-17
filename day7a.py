#!/usr/bin/env python3
from collections import Counter

FIVE_OF_A_KIND = 6
FOUR_OF_A_KIND = 5
FULL_HOUSE = 4
THREE_OF_A_KIND = 3
TWO_PAIR = 2
ONE_PAIR = 1
HIGH_CARD = 0

CARD_TO_BASE13 = {
    "2": 0,
    "3": 1,
    "4": 2,
    "5": 3,
    "6": 4,
    "7": 5,
    "8": 6,
    "9": 7,
    "T": 8,
    "J": 9,
    "Q": 10,
    "K": 11,
    "A": 12,
}


def get_hand_type(hand: str) -> int:
    counter = Counter(hand)
    frequencies = set(counter.values())
    if 5 in frequencies:
        return FIVE_OF_A_KIND
    if 4 in frequencies:
        return FOUR_OF_A_KIND
    if 3 in frequencies and 2 in frequencies:
        return FULL_HOUSE
    if 3 in frequencies:
        return THREE_OF_A_KIND
    if 2 in frequencies:
        pair_count = set(Counter(list(counter.values())).values())
        if 2 in pair_count:
            return TWO_PAIR
        return ONE_PAIR
    return HIGH_CARD


def get_hand_value(hand: str) -> tuple[int, int, int, int, int, int]:
    return (
        get_hand_type(hand),
        CARD_TO_BASE13[hand[0]],
        CARD_TO_BASE13[hand[1]],
        CARD_TO_BASE13[hand[2]],
        CARD_TO_BASE13[hand[3]],
        CARD_TO_BASE13[hand[4]],
    )


with open("input7.txt", "r") as fp:
    lines = fp.read().splitlines()

games = []
for line in lines:
    hand, bid = line.split()
    games.append((hand, int(bid)))

sorted_games = sorted(games, key=lambda x: get_hand_value(x[0]))

result = sum([rank * bid for rank, (_, bid) in enumerate(sorted_games, start=1)])
print(result)
