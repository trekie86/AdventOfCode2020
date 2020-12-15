"""Advent of Code 2020 day 14 part 1"""

import re

def main():

    with open('day14/input.txt', 'r') as f:
        lines = f.read().splitlines()

    register = {}
    mask_command = {}
    for line in lines:
        if line.startswith('mask'):
            mask_command = parse_mask(line)
        else:
            #This should only be a memory operation
            memory_operations = line.split(' = ')
            value = int(memory_operations[1])
            key = list(map(int, re.findall(r'\d+', memory_operations[0])))[0]
            # print(f"Applying mask {mask_command} against operation {memory_operations}")
            apply_register_operation(register=register, mask=mask_command, key=key, value=value)

    print(register)

    print(f"Total: {sum(register.values())}")


def parse_mask(line: str) -> {}:
    mask_commands = {}
    mask_string = list(line.split(' = ')[1])[::-1]
    for i in range(len(mask_string)):
        if mask_string[i] == 'X':
            continue
        else:
            mask_commands[i] = mask_string[i]
    return mask_commands

def apply_register_operation(register: {}, mask: {}, key: str, value: int):
    value_bin = list(format(int(value), 'b').zfill(36))[::-1]

    for k,v in mask.items():
        value_bin[k] = v

    register[key] = int(''.join(value_bin[::-1]), 2)

if __name__ == '__main__':
    main()
