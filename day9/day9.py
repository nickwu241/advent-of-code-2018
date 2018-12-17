#!/usr/bin/env python
from collections import deque
import itertools
import re

with open('input') as f:
    match = re.match(r'(\d+) players; last marble is worth (\d+) points', f.read())
    n_players, highest_marble_points = map(int, match.group(1, 2))

# Puzzle 1
def get_winning_player_score(n_players, highest_marble_points):
    circle = deque([0])
    player_scores = [0] * (n_players + 1)

    players = itertools.cycle(range(1, n_players + 1))
    marbles = range(1, highest_marble_points + 1)
    for player, marble in zip(players, marbles):
        if marble % 23 == 0:
            circle.rotate(-7)
            player_scores[player] += marble + circle.pop()
        else:
            circle.rotate(2)
            circle.append(marble)
    return max(player_scores)

print(get_winning_player_score(n_players, highest_marble_points))

# Puzzle 2
print(get_winning_player_score(n_players, highest_marble_points * 100))
