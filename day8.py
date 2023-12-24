#!/usr/bin/env python3
import re
from functools import reduce
from itertools import count

with open("input8.txt") as fp:
    lines = fp.read().splitlines()

directions = list(lines[0])
navigation = {}
for line in lines[2:]:
    start, remainder = line.split(" = ")
    left, right = remainder[1:-1].split(", ")
    navigation[start] = {"L": left, "R": right}


def navigate(start: str, stop: re.Pattern) -> int:
    position = start
    for i in count():
        if stop.match(position):
            return i
        position = navigation[position][directions[i % len(directions)]]
    raise Exception("Unreachable")


def gcd(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    return a * b // gcd(a, b)


print(f"Part 1: {navigate('AAA', re.compile('ZZZ'))}")

starts = [s for s in navigation.keys() if s.endswith("A")]
path_lengths = [navigate(s, re.compile(r"..Z")) for s in starts]
print(f"Part 2: {reduce(lcm, path_lengths)}")
