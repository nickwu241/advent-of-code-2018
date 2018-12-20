#!/usr/bin/env python
import itertools

with open('input') as f:
    serial_number = int(f.read())

# Puzzle 1
def get_power_level(x, y, serial_number):
    rack_id = x + 10
    power_level = ((rack_id * y) + serial_number) * rack_id
    power_level = (power_level // 100 % 10) - 5
    return power_level

def get_total_power(grid, x, y, x_max, y_max):
    if not (0 < x <= x_max - 2 and 0 < y <= y_max - 2):
        return float('-inf')

    coords_3x3_grid = itertools.product(range(x, x+3), range(y, y+3))
    return sum(grid[y-1][x-1] for x, y in coords_3x3_grid)

assert get_power_level(3, 5, 8) == 4
assert get_power_level(122, 79, 57) == -5
assert get_power_level(217, 196, 39) == 0
assert get_power_level(101, 153, 71) == 4

# 300x300 grid starting at (1,1)
x_max = 300
y_max = 300
grid = [[get_power_level(x, y, serial_number) for x in range(1, x_max+1)] for y in range(1, y_max+1)]
all_coords = itertools.product(range(1, y_max+1), range(1, x_max+1))
_, x, y = max((get_total_power(grid, x, y, x_max, y_max), x, y) for x, y in all_coords)
print(x, y)

# Puzzle 2
