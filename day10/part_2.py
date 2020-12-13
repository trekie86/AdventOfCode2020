"""Advent of Code 2020 day 10 part 2"""

from collections import Counter

def main():
    """The main method"""

    lines = []
    # lines.append(0)
    with open('day10/input.txt', 'r') as f:
        for line in f:
            lines.append(int(line))
    print(f"Original list: {lines}")
    lines = sorted(lines)
    print(f"Sorted list: {lines}")
    # lines.append(lines[-1] + 3)

    cheater(lines)
    # min_value = 0
    # max_value = lines[-1] + 3
    # combinations = []

    # combinations.append(lines)
    # modify_position = 0
    # modify_count = 1
    # while modify_count < len(lines):



def validate_list(lines, min_value, max_value):
    if lines[0] - min_value > 3:
        return False

    if max_value - lines[-1] > 3:
        return False

    for pos in range(1, len(lines)):
        if lines[pos] - lines[pos-1] > 3:
            return False

    return True

def cheater(jolts):

    dp = Counter()
    dp[0] = 1

    for jolt in jolts:
        # print(f"Count of {jolt} = {dp[jolt-1]} + {dp[jolt-2]} + {dp[jolt-3]}")
        dp[jolt] = dp[jolt-1] + dp[jolt-2] + dp[jolt-3]

    print(dp[jolts[-1]])

if __name__ == '__main__':
    main()