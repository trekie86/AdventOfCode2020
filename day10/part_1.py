"""Advent of Code 2020 day 10 part 1"""

def main():
    """The main method"""

    lines = []
    lines.append(0)
    with open('day10/input.txt', 'r') as f:
        for line in f:
            lines.append(int(line))
    print(f"Original list: {lines}")
    lines = sorted(lines)
    print(f"Sorted list: {lines}")
    lines.append(lines[-1]+3)

    one_jolt_delta = 0
    three_jold_delta = 0
    for pos in range(1,len(lines)):
        left = lines[pos-1]
        right = lines[pos]
        delta = right - left
        # print(f"Comparing {left} and {right} with delta of {delta}")
        if delta == 1:
            one_jolt_delta += 1
        elif delta == 3:
            three_jold_delta += 1

    print(f"{one_jolt_delta} one jolt deltas and {three_jold_delta} three jolt deltas")
    print(one_jolt_delta * three_jold_delta)



if __name__ == '__main__':
    main()