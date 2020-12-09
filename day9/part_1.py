"""Advent of Code 2020 day 9 part 1"""

from itertools import combinations

PREAMBLE = 25

def main():
    """The main function"""
    lines = []
    with open('day9/input.txt', 'r') as f:
        for line in f:
            lines.append(int(line))

    for position in range(PREAMBLE, len(lines)):
        if not analyze_slice(lines, position):
            print(f"Invalid at position {position} with value {lines[position]}.")
            break


def analyze_slice(lines, position):
    """Finds the position where the sum of two numbers within the
    preample size don't equal the current position value"""
    possible_combinations = list(combinations(lines[position-PREAMBLE:position], 2))
    match_line = [each for each in possible_combinations if sum(each) == lines[position]]
    return bool(match_line)

if __name__ == "__main__":
    # execute only if run as a script
    main()
