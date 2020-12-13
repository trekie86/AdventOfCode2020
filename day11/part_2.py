"""Advent of Code 2020 day 11 part 2"""

import numpy as np
import copy
from collections import Counter

FLOOR = '.'
OCCUPIED = '#'
EMPTY = 'L'

def main():

    seat_map = []
    with open('day11/sample.txt', 'r') as f:
        for line in f:
            seat_map.append(list(line.strip()))
    np_seat_map = np.array(seat_map)

    occupy_all_seats(np_seat_map)
    print(np_seat_map)
    # print(np_seat_map.shape)
    # print(count_total_occupied(np_seat_map))

    # print(count_visible_adjacent(np_seat_map, 1, 0))

    # #left
    # print(np_seat_map[0,:1])
    # #right
    # print(np_seat_map[0,2:])
    # #up
    # print(np_seat_map[:0,1])
    # #down
    # print(np_seat_map[1:,1])
    new_seat_map = process_occupy_rules(np_seat_map)
    print(new_seat_map)
    print(count_total_occupied(new_seat_map))
    np_seat_map = new_seat_map
    new_seat_map = process_occupy_rules(np_seat_map)
    print(count_total_occupied(new_seat_map))
    # count = 0
    # while True:
    #     count += 1
    #     new_seat_map = process_occupy_rules(np_seat_map)
    #     equal_arrays = np.array_equal(new_seat_map, np_seat_map)
    #     np_seat_map = new_seat_map
    #     if equal_arrays:
    #         break
    #     # print(np_seat_map)
    # print(np_seat_map)
    # print(f"Loop count {count}")
    # print(count_total_occupied(np_seat_map))

def occupy_all_seats(seat_map):
    for i in range(seat_map.shape[0]):
        for j in range(seat_map.shape[1]):
            if seat_map[i,j] == EMPTY:
                seat_map[i,j] = OCCUPIED

def process_occupy_rules(seat_map):
    max_i = seat_map.shape[0]
    max_j = seat_map.shape[1]
    new_map = copy.deepcopy(seat_map)
    for i in range(max_i):
        for j in range(max_j):
            print(f"Checking position {i}/{j} with value {seat_map[i,j]} and visible occupied {count_visible_occupied(seat_map, i, j)}")
            if seat_map[i,j] == EMPTY and count_visible_occupied(seat_map, i, j) == 0:
                new_map[i,j] = OCCUPIED
            elif seat_map[i,j] == OCCUPIED and count_visible_occupied(seat_map, i, j) >= 5:
                new_map[i,j] = EMPTY

    return new_map


def count_visible_occupied(seat_map, i, j):
    max_i = seat_map.shape[0]-1
    max_j = seat_map.shape[1]-1
    # print(f"Max i: {max_i}")
    # print(f"Max j: {max_j}")
    left = np.count_nonzero(seat_map[i,:j] == OCCUPIED) > 0
    right = np.count_nonzero(seat_map[i,j+1:] == OCCUPIED) > 0
    up = np.count_nonzero(seat_map[:i,j] == OCCUPIED) > 0
    down = np.count_nonzero(seat_map[i+1:,j] == OCCUPIED) > 0
    up_left = False
    up_right = False
    for step in range(1, max_i+1):
        # print(f"Current i: {i-step}")
        if i - step < 0:
            break
        if seat_map[max(0,i-step),max(j-step, 0)] == OCCUPIED:
            up_left = True
        if seat_map[max(0,i-step),min(j+step, max_j)] == OCCUPIED:
            up_right = True
    down_left = False
    down_right = False
    for step in range(1,max_i+1):
        # print(f"Current i: {i+step}")
        if i + step > max_i:
            break
        if seat_map[min(i+step, max_i),max(j-step, 0)] == OCCUPIED:
            down_left = True
        if seat_map[min(i+step, max_i),min(j+step, max_j)] == OCCUPIED:
            down_right = True

    return np.count_nonzero([left, right, up, down, up_left, up_right, down_left, down_right])
    # count = np.count_nonzero(seat_map[max(i-1,0):min(i+2, max_i),max(j-1,0):min(j+2, max_j)] == OCCUPIED)
    # if seat_map[i,j] == OCCUPIED:
    #     count -= 1
    # return count

def print_current_seat_config(seat_map, i, j):
    max_i = seat_map.shape[0]
    max_j = seat_map.shape[1]
    print(seat_map[max(i-1,0):min(i+2, max_i),max(j-1,0):min(j+2, max_j)])

def count_total_occupied(seat_map):
    return np.count_nonzero(seat_map == OCCUPIED)

if __name__ == '__main__':
    main()