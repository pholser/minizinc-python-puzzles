from collections import namedtuple


Problem = namedtuple('Problem', ['universe', 'sets'])

CostedSet = namedtuple('CostedSet', ['id', 'cost', 'items'])

Cover = namedtuple('Cover', ['cost', 'sets'])


def parse_problem(input):
    lines = input.split('\n')

    header_pieces = lines[0].split()
    item_count, set_count = int(header_pieces[0]), int(header_pieces[1])

    universe = set()
    sets = []
    for i in range(1, set_count + 1):
        set_parts = lines[i].split()

        next_items = list(int(i) for i in set_parts[1:])
        next_items_as_set = set(next_items)
        assert len(next_items) == len(next_items_as_set)

        next_set = CostedSet(i - 1, int(set_parts[0]), next_items)

        sets.append(next_set)
        universe = universe | set(next_items_as_set)

    return Problem(frozenset(i for i in universe), sets)
