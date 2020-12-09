"""Advent of Code 2020 day 9 part 2"""

from itertools import combinations
import numpy as np

PREAMBLE = 25

def main():
    """The main method"""
    lines = []
    with open('day9/input.txt', 'r') as f:
        for line in f:
            lines.append(int(line))

    result = 0
    for position in range(PREAMBLE, len(lines)):
        result = analyze_slice(lines, position)
        if result:
            print(f"Starting analysis at position {position} against value {lines[position]}.")
            break
    calc_value = lines[result]
    for min_pos in range(result):
        for max_pos in range(min_pos+1,result):
            summed_val = np.sum(lines[min_pos:max_pos+1])
            if summed_val > calc_value:
                print(f"Short circuit, faster")
                break
            elif summed_val == calc_value:
                min_value = np.min(lines[min_pos:max_pos+1])
                max_value = np.max(lines[min_pos:max_pos+1])
                print(f"min pos={min_pos}, max pos={max_pos}, min value {min_value} and max \
                value {max_value}, resulting sum of {min_value+max_value}")
                return


def analyze_slice(lines, position):
    """Finds the position where the sum of two numbers within
    the preample size don't equal the current position value"""
    possible_combinations = list(combinations(lines[position-PREAMBLE:position], 2))
    li = [each for each in possible_combinations if sum(each) == lines[position]]
    if not li:
        return position
    else:
        return None


if __name__ == "__main__":
    # execute only if run as a script
    main()
