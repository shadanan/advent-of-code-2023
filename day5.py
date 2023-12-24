#!/usr/bin/env python3
from dataclasses import dataclass


def intersects(start: int, stop: int, value: int) -> bool:
    return start <= value < stop


def transfer(source: int, dest: int, length: int, value: int) -> int:
    assert intersects(source, source + length, value)
    return dest + value - source


@dataclass
class Range:
    start: int
    length: int

    def __contains__(self, i: int) -> bool:
        return intersects(self.start, self.start + self.length, i)


@dataclass
class Map:
    source: Range
    dest: Range

    def forward(self, i: int) -> int:
        return transfer(self.source.start, self.dest.start, self.source.length, i)

    def reverse(self, j: int) -> int:
        return transfer(self.dest.start, self.source.start, self.source.length, j)

    @staticmethod
    def parse(line: str) -> "Map":
        dest, source, length = [int(v) for v in line.split()]
        return Map(Range(source, length), Range(dest, length))


@dataclass
class Recipe:
    name: str
    maps: list[Map]

    def dest_boundaries(self) -> list[int]:
        return [map.dest.start for map in self.maps]

    def forward(self, i: int) -> int:
        for map in self.maps:
            if i in map.source:
                return map.forward(i)
        return i

    def reverse(self, j: int) -> int:
        for map in self.maps:
            if j in map.dest:
                return map.reverse(j)
        return j

    @staticmethod
    def parse(recipe: str) -> "Recipe":
        lines = recipe.splitlines()
        return Recipe(lines[0], [Map.parse(line) for line in lines[1:]])


@dataclass
class Almanac:
    recipes: list[Recipe]

    def forward(self, i: int) -> int:
        for recipe in self.recipes:
            i = recipe.forward(i)
        return i

    def reverse(self, j: int) -> int:
        for recipe in reversed(self.recipes):
            j = recipe.reverse(j)
        return j

    @staticmethod
    def parse(instructions: list[str]) -> "Almanac":
        recipes = [Recipe.parse(instruction) for instruction in instructions]
        return Almanac(recipes)


@dataclass
class SeedRanges:
    ranges: list[Range]

    def __contains__(self, i: int) -> bool:
        return any(i in range for range in self.ranges)

    def bounds(self) -> set[int]:
        return {range.start for range in self.ranges}


with open("input5.txt", "r") as fp:
    data = fp.read().split("\n\n")


seeds = [int(v) for v in data[0].strip().split()[1:]]
almanac = Almanac.parse(data[1:])
print(f"Part 1: {min([almanac.forward(seed) for seed in seeds])}")

all_bounds = set()
for recipe in reversed(almanac.recipes):
    all_bounds.update(recipe.dest_boundaries())
    all_bounds = {recipe.reverse(v) for v in all_bounds}

seed_ranges = SeedRanges(
    [Range(seeds[i], seeds[i + 1]) for i in range(0, len(seeds), 2)]
)
bounds = {v for v in all_bounds if v in seed_ranges} | seed_ranges.bounds()
print(f"Part 2: {min([almanac.forward(bound) for bound in bounds])}")
