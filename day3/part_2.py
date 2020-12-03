"""Advent of Code 2020 day 3 part 1"""

from numpy import *
from math import prod

def find_trees(move_h: int, move_v: int) -> int:
    map = []

    with open("day3/input.txt", "r") as f:
        for line in f.readlines():
            map.append(list(line.strip()))
    trees = 0
    current_pos_h = 0
    current_pos_v = 0

    while True:
        if(current_pos_h + move_h > len(map[current_pos_v])-1):
            current_pos_h += move_h - len(map[current_pos_v])
        else:
            current_pos_h += move_h

        if(current_pos_v + move_v > len(map)-1):
            break
        else:
            current_pos_v += move_v

        # print(f"Checking position h: {current_pos_h} & v: {current_pos_v}")
        if(map[current_pos_v][current_pos_h] == '#'):
            trees += 1

    return trees
    print(map)


results = []
results.append(find_trees(1,1))
results.append(find_trees(3,1))
results.append(find_trees(5,1))
results.append(find_trees(7,1))
results.append(find_trees(1,2))

print(prod(results))