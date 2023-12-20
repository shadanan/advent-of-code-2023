#!/usr/bin/env python3
import numpy as np

with open("input9.txt") as fp:
    lines = fp.read().splitlines()


histories: list[np.ndarray] = []
for line in lines:
    histories.append(np.array([int(x) for x in line.split()]))


def difference(history: np.ndarray) -> np.ndarray:
    return history[1:] - history[:-1]


def extrapolate_forward(history: np.ndarray) -> int:
    values = []
    while np.any(history != 0):
        values.append(history[-1])
        history = difference(history)
    return sum(values)


def extrapolate_backward(history: np.ndarray) -> int:
    values = []
    sign = 1
    while np.any(history != 0):
        values.append(sign * history[0])
        sign = sign * -1
        history = difference(history)
    return sum(values)


print("Part 1:", sum([extrapolate_forward(h) for h in histories]))
print("Part 2:", sum([extrapolate_backward(h) for h in histories]))
