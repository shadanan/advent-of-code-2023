#!/usr/bin/env python3

with open("input2a.txt", "r") as fp:
    lines = fp.read().strip().splitlines()

sum_power = 0
for line in lines:
    game_str, remainder = line.split(": ")
    game_id = int(game_str.split()[-1])
    game = remainder.replace("; ", ", ").split(", ")
    
    max_colors = {'red': 0, 'green': 0, 'blue': 0}
    for color_count in game:
        count, color = color_count.split()
        count = int(count)
        if max_colors[color] < count:
            max_colors[color] = count
    
    # Compute the product of all values
    power = 1    
    for value in max_colors.values():
        power *= value
    
    sum_power += power
    
print(sum_power)

