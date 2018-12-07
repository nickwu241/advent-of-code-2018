#!/usr/bin/env python
from collections import Counter
import re
import string

STEP_RE = re.compile(r'Step (\w) must be finished before step (\w) can begin.')

with open('input') as f:
    step_dependencies = [STEP_RE.match(line).group(1, 2) for line in f]

# Puzzle 1
# Steps are only uppercase letters.
step_to_preqs = {letter: set() for letter in string.ascii_uppercase}
preq_to_steps = {letter: set() for letter in string.ascii_uppercase}
for preq_step, step in step_dependencies:
    step_to_preqs[step].add(preq_step)
    preq_to_steps[preq_step].add(step)

while step_to_preqs:
    next_step = min(step for step, preqs in step_to_preqs.items() if not preqs)
    print(next_step, end='')

    step_to_preqs.pop(next_step)
    for step in preq_to_steps[next_step]:
        step_to_preqs[step].remove(next_step)
print()

# Puzzle 2
step_to_preqs = {letter: set() for letter in string.ascii_uppercase}
preq_to_steps = {letter: set() for letter in string.ascii_uppercase}
timers = {
    letter: ord(letter) - ord('A') + 60 + 1
    for letter in string.ascii_uppercase
}
for preq_step, step in step_dependencies:
    step_to_preqs[step].add(preq_step)
    preq_to_steps[preq_step].add(step)

seconds_elpased = 0
workers = [None] * 5
while timers:
    # Distribute work.
    for i, worker in enumerate(workers):
        if worker is not None:
            continue

        try:
            next_steps = (step for step, preqs in step_to_preqs.items()
                                if not preqs and step not in workers)
            next_step = min(next_steps)
            workers[i] = next_step
        except ValueError:
            # No work to assign to any workers.
            break

    # Do the work.
    for i, worker in enumerate(workers):
        if worker is None:
            continue
        timers[worker] -= 1
        if timers[worker] != 0:
            continue

        # Worker has compelted the step.
        timers.pop(worker)
        step_completed = worker
        workers[i] = None
        step_to_preqs.pop(step_completed)
        for step in preq_to_steps[step_completed]:
            step_to_preqs[step].remove(step_completed)

    # Increment the time
    seconds_elpased += 1
print(seconds_elpased)