#!/usr/bin/env python3

from dataclasses import dataclass

with open("input5.txt", "r") as fp:
    recipe = fp.read().split("\n\n")


@dataclass
class Mapping:
    name: str
    ranges: list[tuple[int, int, int]]

    def get(self, i: int) -> int:
        for source_start, source_end, dest_start in self.ranges:
            if source_start <= i < source_end:
                return i - source_start + dest_start
        return i


def parse_mapping(lines: list[str]) -> Mapping:
    """Parse a mapping, e.g."""
    name = lines[0].split()[0]
    ranges = []
    for line in lines[1:]:
        dest_start, source_start, source_length = [int(v) for v in line.split()]
        ranges.append((source_start, source_start + source_length, dest_start))
    return Mapping(name, ranges)


def apply_pipeline(seed: int, pipeline: list[Mapping]) -> int:
    result = seed
    for mapper in pipeline:
        result = mapper.get(result)
    return result


seeds = [int(v) for v in recipe[0].strip().split()[1:]]
pipeline = [parse_mapping(instruction.splitlines()) for instruction in recipe[1:]]
print(min([apply_pipeline(seed, pipeline) for seed in seeds]))
