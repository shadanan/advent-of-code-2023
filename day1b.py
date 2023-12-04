#!/usr/bin/env python3

with open("input1.txt") as f:
    lines = (
        f.read()
        .replace("zero", "ze0ro")
        .replace("one", "on1e")
        .replace("two", "tw2o")
        .replace("three", "thr3ee")
        .replace("four", "fo4ur")
        .replace("five", "fi5ve")
        .replace("six", "si6x")
        .replace("seven", "sev7en")
        .replace("eight", "eig8ht")
        .replace("nine", "ni9ne")
        .splitlines()
    )

calibration_sum = 0
for line in lines:
    digits = [char for char in line if char.isdigit()]
    calibration = int(digits[0] + digits[-1])
    calibration_sum += calibration
print(calibration_sum)
