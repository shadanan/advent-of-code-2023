#!/usr/bin/env python3
import math


def ways_to_beat_record(race_duration_ms: int, record_ms: int) -> int:
    discriminant = math.sqrt(race_duration_ms**2 - 4 * record_ms)
    left_bound = (race_duration_ms - discriminant) / 2
    right_bound = (race_duration_ms + discriminant) / 2
    if int(discriminant) ** 2 == race_duration_ms**2 - 4 * record_ms:
        return math.floor(right_bound) - math.ceil(left_bound) - 1
    return math.floor(right_bound) - math.ceil(left_bound) + 1


with open("input6.txt", "r") as fp:
    lines = fp.read().splitlines()

races = zip(
    [int(x) for x in lines[0].split()[1:]],
    [int(x) for x in lines[1].split()[1:]],
)

result = math.prod(
    [ways_to_beat_record(duration, record) for duration, record in races]
)
print(f"Day 6a: {result}")
print(f"Day 6b: {ways_to_beat_record(34908986, 204171312101780)}")
