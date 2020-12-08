"""Advent of Code 2020 Day 8 part 1"""

def read_file_to_lines():
    """Read the file and convert it to a list of tuples"""
    lines = []
    with open('day8/input.txt', 'r') as f:
        for line in f:
            str_parts = line.strip().split()
            lines.append((str_parts[0], int(str_parts[1])))
    # print(lines)
    return lines

def test_program_run(lines):
    """Run the program instructions through and see if it completes to the end"""
    accumulator = 0
    instruc = 0
    steps_run = set([])
    while True:
        if instruc > len(lines) - 1:
            print(f"Reached the end of the instructions!")
            print(accumulator)
            return True
        elif instruc in steps_run:
            print(f"We received a duplicate instruction at step {instruc}")
            return False
        else:
            # print(f"Running step {instruc}")
            # print(f"Running {lines[instruc]}")
            steps_run.add(instruc)
        action = lines[instruc][0]
        if action == 'nop':
            instruc += 1
        elif action == 'acc':
            accumulator += lines[instruc][1]
            instruc += 1
        else:
            instruc += lines[instruc][1]


def main():
    """The main function"""
    orig_lines = read_file_to_lines()

    for changed_instruction in range(len(orig_lines)):
        lines = orig_lines.copy()
        if lines[changed_instruction][0] == 'nop':
            print(f"Changing instruction {changed_instruction} from 'nop' to 'jmp'")
            l1 = list(lines[changed_instruction])
            l1[0] = 'jmp'
            lines[changed_instruction] = tuple(l1)
        elif lines[changed_instruction][0] == 'jmp':
            print(f"Changing instruction {changed_instruction} from 'jmp' to 'nop'")
            l1 = list(lines[changed_instruction])
            l1[0] = 'nop'
            lines[changed_instruction] = tuple(l1)
        else:
            continue

        if test_program_run(lines):
            break





if __name__ == "__main__":
    # execute only if run as a script
    main()
