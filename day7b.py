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
    "Q": 10,
    "K": 11,
    "A": 12,
}


def get_hand_type(hand: str) -> int:
    counter = Counter(hand)
    frequencies = set(counter.values())
    if 5 in frequencies:
        # 22222
        # JJJJJ
        return FIVE_OF_A_KIND
    if 4 in frequencies:
        # 22223
        # 2222J
        # JJJJ2
        if "J" in counter:
            return FIVE_OF_A_KIND
        return FOUR_OF_A_KIND
    if 3 in frequencies and 2 in frequencies:
        # JJ222 -> 22222
        # JJJ22 -> 22222
        if "J" in counter:
            return FIVE_OF_A_KIND
        return FULL_HOUSE
    if 3 in frequencies:
        # JJJ23
        # 222J3
        if counter["J"] == 1:
            return FOUR_OF_A_KIND
        return THREE_OF_A_KIND
    if 2 in frequencies:
        if len(counter) == 3:
            # 22334
            # 2233J
            # 22JJ4
            if counter["J"] == 2:
                return FOUR_OF_A_KIND
            if counter["J"] == 1:
                return FULL_HOUSE
            return TWO_PAIR
        # 22345
        # 2234J
        # 234JJ
        if "J" in counter:
            return THREE_OF_A_KIND
        return ONE_PAIR
    # 23456
    # 2345J
    if "J" in counter:
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
