#!/usr/bin/env python
from collections import defaultdict
from datetime import datetime
import itertools
import operator
import re

LOG_RE = re.compile(r'\[(.*)\] (Guard #\d+|wakes up|falls asleep)')
TIMESTAMP_FMT = '%Y-%m-%d %H:%M'

def parse_line(line):
    match = LOG_RE.match(line)
    ts, info = match.group(1, 2)
    if info.startswith('Guard'):
        info = int(info[info.find('#') + 1:])
    return (datetime.strptime(ts, TIMESTAMP_FMT), info)

with open('input') as f:
    event_log = sorted(parse_line(line) for line in f)

# Puzzle 1
guard_sleep_times = defaultdict(lambda: [0]*59)
for ts, info in event_log:
    if info == 'falls asleep':
        minute_last_asleep = ts.minute
    elif info == 'wakes up':
        for minute in range(minute_last_asleep, ts.minute):
            guard_sleep_times[current_guard_on_shift][minute] += 1
    else: # A new guard came on shift.
        current_guard_on_shift = info

_, guard_id = max((sum(asleep_array), guard_id) for guard_id, asleep_array in guard_sleep_times.items())
minute_slept_most, _ = max(enumerate(guard_sleep_times[guard_id]), key=operator.itemgetter(1))
print(guard_id * minute_slept_most)

# Puzzle 2
running_max = 0
for guard_id, asleep_array in guard_sleep_times.items():
    minute, max_asleep = max(enumerate(asleep_array), key=operator.itemgetter(1))
    if max_asleep > running_max:
        running_max = max_asleep
        running_max_minute = minute
        guard_id_asleep_most_frequent = guard_id

print(guard_id_asleep_most_frequent * running_max_minute)
