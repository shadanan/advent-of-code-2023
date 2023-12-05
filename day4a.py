#!/usr/bin/env python3

with open("input4.txt", "r") as fp:
    lines = fp.read().strip().splitlines()

if __name__ == "__main__":
    points_sum = 0
    for line in lines:
        _, numbers = line.split(": ")
        left, right = numbers.split(" | ")
        winning_numbers_set = {n for n in left.split()}
        my_numbers_set = {n for n in right.split()}
        intersection = winning_numbers_set.intersection(my_numbers_set)
        points = 2 ** (len(intersection) - 1) if len(intersection) > 0 else 0
        points_sum += points
    print(points_sum)