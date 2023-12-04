#!/usr/bin/env python3

RULES = {
    "red": 12,
    "green": 13,
    "blue": 14,
}

with open("input2.txt", "r") as fp:
    lines = fp.read().strip().splitlines()


def is_possible(game):
    for roll in game:
        value, color = roll.split()
        value = int(value)
        if value > RULES[color]:
            return False
    return True


total = 0
for line in lines:
    game_str, remainder = line.split(": ")
    game_id = int(game_str.split()[-1])
    game = remainder.replace("; ", ", ").split(", ")
    if is_possible(game):
        total += game_id
print(total)
