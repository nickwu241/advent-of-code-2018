#!/usr/bin/env python
from collections import Counter

with open('input') as f:
    lines = [line.strip() for line in f]

# Puzzle 1
n_boxes_letters_exactly_twice = 0
n_boxes_letters_exactly_three_times = 0
for counter in (Counter(line) for line in lines):
    if any(c == 2 for c in counter.values()):
        n_boxes_letters_exactly_twice += 1
    if any(c == 3 for c in counter.values()):
        n_boxes_letters_exactly_three_times += 1

checksum = n_boxes_letters_exactly_twice * n_boxes_letters_exactly_three_times
print(checksum)

# Puzzle 2
def get_common_letters(box_ids):
    for i, box_id1 in enumerate(box_ids):
        for box_id2 in box_ids[i+1:]:
            diff = [j for j, (c1, c2) in enumerate(zip(box_id1, box_id2))
                    if c1 != c2]
            if len(diff) == 1:
                diff_i = diff[0]
                return box_id1[:diff_i] + box_id1[diff_i+1:]

print(get_common_letters(lines))
