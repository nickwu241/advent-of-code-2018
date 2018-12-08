#!/usr/bin/env python
with open('input') as f:
    data = [int(num) for num in f.read().split()]

# Puzzle 1
def get_node_metadataa(stream):
    n_childs = next(stream)
    n_metadata = next(stream)
    for _ in range(n_childs):
        yield from get_node_metadataa(stream)
    for _ in range(n_metadata):
        yield next(stream)

print(sum(get_node_metadataa(iter(data))))

# Puzzle 2
def get_node_value(stream):
    n_childs = next(stream)
    n_metadata = next(stream)
    if n_childs == 0:
        return sum(next(stream) for _ in range(n_metadata))

    child_data = [get_node_value(stream) for _ in range(n_childs)]
    total = 0
    for _ in range(n_metadata):
        try:
            total += child_data[next(stream)-1]
        except IndexError:
            pass
    return total

print(get_node_value(iter(data)))