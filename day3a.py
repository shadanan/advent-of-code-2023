#!/usr/bin/env python3
import re
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


def find_part_numbers(lines: list[str]) -> list[PartNumber]:
    part_numbers = []
    for row, line in enumerate(lines):
        for match in NUMBER_PATERN.finditer(line):
            pn = PartNumber(row, match.start(), match.end(), int(match.group()))
            if is_valid(lines, pn):
                part_numbers.append(pn)
    return part_numbers


def is_valid(lines, part_number: PartNumber) -> bool:
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


if __name__ == "__main__":
    print(sum([pn.value for pn in find_part_numbers(lines)]))
