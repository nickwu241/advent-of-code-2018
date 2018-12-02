#!/usr/bin/env python
import itertools

with open('input') as f:
    frequency_detlas = [int(line) for line in f]

# Puzzle 1
print(sum(frequency_detlas))

# Puzzle 2
current_frequency = 0
seen = set()
for df in itertools.cycle(frequency_detlas):
    current_frequency += df
    if current_frequency in seen:
        print(current_frequency)
        break
    seen.add(current_frequency)
