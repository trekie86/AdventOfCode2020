"""Advent of Code 2020 day 13 part 2"""

import numpy as np
import math

def main():
    with open('day13/input.txt', 'r') as f:
        raw_input = f.read().splitlines()
        busses = raw_input[1].split(',')

    print(f"Available busses: {busses}")

    first_time = find_subsequent_busses(busses)
    print(f"Earliest subsequent timestamp: {first_time}")


def find_subsequent_busses(busses):
    time = 0
    step = int(busses[0])

    for bus in busses[1:]:
        if bus == 'x':
            continue
        else:
            while True:
                if (time + busses.index(bus)) % int(bus) == 0:
                    break
                time += step
            step = np.lcm(step, int(bus))
    #We have reached the happy place
    return time

if __name__ == '__main__':
    main()