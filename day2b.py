#!/usr/bin/env python3
from collections import defaultdict
from math import prod

with open("input2.txt", "r") as fp:
    lines = fp.read().strip().splitlines()

sum_power = 0
for line in lines:
    game_str, remainder = line.split(": ")
    game_id = int(game_str.split()[-1])
    game = remainder.replace("; ", ", ").split(", ")

    max_colors = defaultdict(int)
    for color_count in game:
        count, color = color_count.split()
        count = int(count)
        if max_colors[color] < count:
            max_colors[color] = count

    # Compute the sum of product of all values
    sum_power += prod(max_colors.values())

print(sum_power)
