#!/usr/bin/env python3
import re
from collections import defaultdict
from dataclasses import dataclass

NUMBER_PATERN = re.compile(r"\d+")

with open("input3.txt", "r") as fp:
    lines = fp.read().strip().splitlines()


@dataclass
class PartNumber:
    row: int
    start: int
    end: int
    value: int


def find_maybe_part_numbers(lines: list[str]) -> list[PartNumber]:
    part_numbers = []
    for row, line in enumerate(lines):
        for match in NUMBER_PATERN.finditer(line):
            part_numbers.append(
                PartNumber(row, match.start(), match.end(), int(match.group()))
            )
    return part_numbers


def get_neighbor_positions(lines, part_number: PartNumber) -> list[tuple[int, int]]:
    neighbors = [
        (part_number.row, part_number.start - 1),
        (part_number.row, part_number.end),
    ]
    for col in range(part_number.start - 1, part_number.end + 1):
        neighbors.append((part_number.row - 1, col))
        neighbors.append((part_number.row + 1, col))

    # Filter out invalid neighbors
    valid_neighbors = []
    for r, c in neighbors:
        if r >= 0 and r < len(lines) and c >= 0 and c < len(lines[0]):
            valid_neighbors.append((r, c))
    return valid_neighbors


if __name__ == "__main__":
    neighbor_part_number_map = defaultdict(list)
    for maybe_part_number in find_maybe_part_numbers(lines):
        neighbors = get_neighbor_positions(lines, maybe_part_number)
        for neighbor in neighbors:
            neighbor_part_number_map[neighbor].append(maybe_part_number)

    gear_ratios = 0
    for r, c in neighbor_part_number_map:
        parts = neighbor_part_number_map[(r, c)]
        if lines[r][c] == "*" and len(parts) >= 2:
            gear_ratio = parts[0].value * parts[1].value
            gear_ratios += gear_ratio
    print(gear_ratios)
