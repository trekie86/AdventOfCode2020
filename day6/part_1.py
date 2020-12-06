"""Advent of Code 2020 Day 6 part 1"""


def main():
    """The main method"""
    flight_groups = []
    with open('day6/input.txt', 'r') as f:
        group = set([])
        for line in f:
            if line.strip() == '':
                flight_groups.append(group)
                group = set([])
            else:
                group.update(set(list(line.strip())))
        flight_groups.append(group)

    count = 0
    for group in flight_groups:
        count += len(group)
    print(count)

if __name__ == "__main__":
    # execute only if run as a script
    main()
