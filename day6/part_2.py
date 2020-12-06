"""Advent of Code 2020 Day 6 part 2"""


def main():
    """The main method"""
    flight_groups = []
    with open('day6/input.txt', 'r') as f:
        group = []
        for line in f:
            if line.strip() == '':
                flight_groups.append(group)
                group = []
            else:
                group.append(list(line.strip()))
        flight_groups.append(group)

    result = []
    for group in flight_groups:
        result.append(set(group[0]).intersection(*group))

    count = 0
    for val in result:
        count += len(val)
    print(count)

if __name__ == "__main__":
    # execute only if run as a script
    main()
