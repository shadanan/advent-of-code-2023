#!/usr/bin/env python3

with open("input1.txt") as f:
    lines = f.read().splitlines()

calibration_sum = 0
for line in lines:
    digits = [char for char in line if char.isdigit()]
    calibration = int(digits[0] + digits[-1])
    calibration_sum += calibration
print(calibration_sum)
