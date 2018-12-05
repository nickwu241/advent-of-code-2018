#!/usr/bin/env python
import string

with open('input') as f:
    s = f.read()

# Puzzle 1
def get_after_reaction_length(s):
    stack = []
    for char in s:
        if stack and abs(ord(stack[-1]) - ord(char)) == 32:
            stack.pop()
        else:
            stack.append(char)
    return len(stack)

print(get_after_reaction_length(s))

# Puzzle 2
running_min = len(s)
for lower, upper in zip(string.ascii_lowercase, string.ascii_uppercase):
    seq = (char for char in s if char != lower and char != upper)
    running_min = min(running_min, get_after_reaction_length(seq))
print(running_min)