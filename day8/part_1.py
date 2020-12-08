"""Advent of Code 2020 Day 8 part 1"""

def read_file_to_lines():
    """Read the file and convert it to a list of tuples"""
    lines = []
    with open('day8/input.txt', 'r') as f:
        for line in f:
            str_parts = line.strip().split()
            lines.append((str_parts[0], int(str_parts[1])))
    return lines


def main():
    """The main function"""
    lines = read_file_to_lines()

    accumulator = 0
    instruc = 0
    steps_run = set([])
    while True:
        if instruc in steps_run:
            print(f"Attempting to run step {instruc} a second time! Stopping!")
            break
        else:
            steps_run.add(instruc)
        action = lines[instruc][0]
        if action == 'nop':
            instruc += 1
        elif action == 'acc':
            accumulator += lines[instruc][1]
            instruc += 1
        else:
            instruc += lines[instruc][1]

    print(accumulator)




if __name__ == "__main__":
    # execute only if run as a script
    main()
