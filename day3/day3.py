#!/usr/bin/env python
import re

def parse_line(line, parse_re=re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')):
    match = parse_re.match(line)
    return [int(g) for g in match.group(1, 2, 3, 4, 5)]

with open('input') as f:
    data_lines = [parse_line(line) for line in f]

# Puzzle 1
grid = [[0 for _ in range(1000)] for _ in range(1000)]
for data in data_lines:
    _, il, it, w, h = data
    for i in range(it, it+h):
        for j in range(il, il+w):
            grid[i][j] += 1

area = sum(1 for row in grid
             for cell in row
             if cell > 1)
print(area)

# Puzzle 2
def get_claim_no_overlap(d):
    claim_id, il, it, w, h = d
    for i in range(it, it+h):
        for j in range(il, il+w):
            if grid[i][j] != 1:
                return None
    return claim_id

for data in data_lines:
    claim_id = get_claim_no_overlap(data)
    if claim_id:
        print(claim_id)
        break
