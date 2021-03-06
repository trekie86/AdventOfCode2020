"""Advent of Code 2020 day 17 part 2"""

from collections import defaultdict
from itertools import product
import operator

INACTIVE = '.'
ACTIVE = '#'
CYCLES = 6

OFFSET_LIST = list(product((-1,0,1), repeat=4))
OFFSET_LIST.remove((0,0,0,0))

def default_val():
    return INACTIVE

def main():
    with open('day17/input.txt', 'r') as f:
        lines = f.read().splitlines()

    grid_map = load_initial_dataset(lines)
    print(count_active(grid_map))
    # print(count_active(cycle(grid_map)))
    for i in range(CYCLES):
        print(f"Cycle # {i+1}")
        grid_map = cycle(grid_map)
        print(count_active(grid_map))


def load_initial_dataset(lines):
    # grid_map = defaultdict(default_val)
    grid_map = {}
    # We presume the first record is 0,0,0 and then add from there
    z = 0
    w = 0
    for y in range(len(lines)):
        row = list(lines[y])
        for x in range(len(row)):
            grid_map[(x,y,z,w)] = row[x]

    # print(grid_map)
    return grid_map

def cycle(grid_map):
    new_grid_map = grid_map.copy()

    #This is only cycling the existing keys, but we need to move outside of the active as well
    outskirt_idx = get_min_max(grid_map)
    for x in range(outskirt_idx[0][0], outskirt_idx[0][1]+1):
        for y in range(outskirt_idx[1][0],outskirt_idx[1][1]+1):
            for z in range(outskirt_idx[2][0],outskirt_idx[2][1]+1):
                for w in range(outskirt_idx[3][0],outskirt_idx[3][1]+1):
                    v = grid_map.get((x,y,z,w), INACTIVE)
                    active_neighbors = count_active_neighbors((x,y,z,w), grid_map)
                    if v == ACTIVE and (active_neighbors < 2 or active_neighbors > 3):
                        new_grid_map[(x,y,z,w)] = INACTIVE
                    elif v == INACTIVE and active_neighbors == 3:
                        new_grid_map[(x,y,z,w)] = ACTIVE

    return new_grid_map

def get_min_max(grid_map):
    keys_list = list(grid_map.keys())
    xs = set([])
    ys = set([])
    zs = set([])
    ws = set([])
    for key in keys_list:
        xs.add(key[0])
        ys.add(key[1])
        zs.add(key[2])
        ws.add(key[3])
    xs = sorted(xs)
    ys = sorted(ys)
    zs = sorted(zs)
    ws = sorted(ws)

    return (min(xs)-1, max(xs)+1), (min(ys)-1, max(ys)+1), (min(zs)-1, max(zs)+1), (min(ws)-1, max(ws)+1)


def count_active(grid_map):
    return len([x for x in grid_map.values() if x == ACTIVE])

def count_active_neighbors(k,grid_map):
    # TODO, this is a dummy method now
    iterable_list = [tuple(map(operator.add, a, k)) for a in OFFSET_LIST]
    return len([a for a in iterable_list if grid_map.get(a) == ACTIVE])


if __name__ == '__main__':
    main()