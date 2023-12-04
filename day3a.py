#!/usr/bin/env python3
from dataclasses import dataclass
import re

NUMBER_PATERN = re.compile(r"\d+")

with open("input3a.txt", "r") as fp:
    lines = fp.read().strip().splitlines()
@dataclass
class PartNumber:
    row: int
    start: int
    end: int
    value: int

def find_maybe_part_numbers(lines: list[str]) -> list[PartNumber]:
    nums = []
    for row, line in enumerate(lines):
        for match in NUMBER_PATERN.finditer(line):
            nums.append(PartNumber(row, match.start(), match.end(), int(match.group())))
    return nums

def is_valid(lines, part_number: PartNumber) -> list[tuple[int, int]]:
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
    
    # Check if neighbors contains a symbol
    for r, c in valid_neighbors:
        if not lines[r][c].isnumeric() and lines[r][c] != ".":
            return True
    return False

if __name__ == '__main__':
    total = 0
    for maybe_part_number in find_maybe_part_numbers(lines):
        if is_valid(lines, maybe_part_number):
            total += maybe_part_number.value
    print(total)
