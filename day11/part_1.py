"""Advent of Code 2020 day 11 part 1"""

import numpy as np
import copy
from collections import Counter

FLOOR = '.'
OCCUPIED = '#'
EMPTY = 'L'

def main():

    seat_map = []
    with open('day11/input.txt', 'r') as f:
        for line in f:
            seat_map.append(list(line.strip()))
    np_seat_map = np.array(seat_map)

    occupy_all_seats(np_seat_map)

    while True:
        new_seat_map = process_occupy_rules(np_seat_map)
        equal_arrays = np.array_equal(new_seat_map, np_seat_map)
        np_seat_map = new_seat_map
        if equal_arrays:
            break
        # print(np_seat_map)
    print(np_seat_map)
    print(count_total_occupied(np_seat_map))

def occupy_all_seats(seat_map):
    for i in range(len(seat_map)):
        for j in range(len(seat_map[0])):
            if seat_map[i,j] == EMPTY:
                seat_map[i,j] = OCCUPIED

def process_occupy_rules(seat_map):
    max_i = seat_map.shape[0]
    max_j = seat_map.shape[1]
    new_map = np.copy(seat_map)
    for i in range(max_i):
        for j in range(max_j):
            if seat_map[i,j] == EMPTY and count_occupied_adjacent(seat_map, i, j) == 0:
                new_map[i,j] = OCCUPIED
            elif seat_map[i,j] == OCCUPIED and count_occupied_adjacent(seat_map, i, j) >= 4:
                new_map[i,j] = EMPTY

    return new_map


def count_occupied_adjacent(seat_map, i, j):
    max_i = seat_map.shape[0]
    max_j = seat_map.shape[1]
    count = np.count_nonzero(seat_map[max(i-1,0):min(i+2, max_i),max(j-1,0):min(j+2, max_j)] == OCCUPIED)
    if seat_map[i,j] == OCCUPIED:
        count -= 1
    return count

def print_current_seat_config(seat_map, i, j):
    max_i = seat_map.shape[0]
    max_j = seat_map.shape[1]
    print(seat_map[max(i-1,0):min(i+2, max_i),max(j-1,0):min(j+2, max_j)])

def count_total_occupied(seat_map):
    return np.count_nonzero(seat_map == OCCUPIED)

if __name__ == '__main__':
    main()