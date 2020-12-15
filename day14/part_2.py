"""Advent of Code 2020 day 14 part 2"""

import re
from itertools import product

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
        if mask_string[i] == '0':
            continue
        else:
            mask_commands[i] = mask_string[i]
    return mask_commands

def apply_register_operation(register: {}, mask: {}, key: str, value: int):
    key_bin = list(format(int(key), 'b').zfill(36))[::-1]

    # Applies 1s and Xs
    for k,v in mask.items():
        key_bin[k] = v

    print(''.join(key_bin[::-1]))
    keys = generate_patterns(key_bin[::-1])

    for x in keys:
        register[int(x, 2)] = value

    # register[str(int(''.join(key_bin[::-1]), 2))] = value

def generate_patterns(keys):

    binary_options = '10'

    # Convert input string into a list so we can easily substitute letters
    seq = list(keys)

    # Find indices of key letters in seq
    indices = [ i for i, c in enumerate(seq) if c == 'X' ]
    results = []
    # Generate key letter combinations & place them into the list
    for t in product(binary_options, repeat=len(indices)):
        for i, c in zip(indices, t):
            seq[i] = c
        results.append(''.join(seq))
    return results

if __name__ == '__main__':
    main()
