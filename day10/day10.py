#!/usr/bin/env python
import re

with open('input') as f:
    position_velocity_list = [tuple(map(int, re.findall(r'-?\d+', line))) for line in f]

# Puzzle 1
for seconds in range(100000):
    min_y = min(y + (dy * seconds) for _, y, _, dy in position_velocity_list)
    max_y = max(y + (dy * seconds) for _, y, _, dy in position_velocity_list)
    diff_y = max_y - min_y
    if diff_y <= 9:
        break

final_positions = [
    (x + (dx * seconds), y + (dy * seconds))
    for x, y, dx, dy in position_velocity_list
]
min_x, _ = min(final_positions)
max_x, _ = max(final_positions)
diff_x = max_x - min_x

grid = [['.' for _ in range(diff_x + 1)] for _ in range(diff_y + 1)]
for x, y in final_positions:
    nx, ny = x - min_x, y - min_y
    grid[ny][nx] = '#'

for row in grid:
    print(''.join(row))

# Puzzle 2
print(seconds)
