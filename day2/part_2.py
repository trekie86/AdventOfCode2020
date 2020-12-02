"""Advent of Code 2020 day 2 part 2"""

passwords = []
with open("day2/input.txt", "r") as f:
    passwords = f.read().splitlines()

valid_pass = 0
print(f"Validating {len(passwords)} passwords.")
for combo in passwords:
    pieces = combo.split(':')
    syntax = pieces[0].strip()
    pass_val = pieces[1].strip()
    # print(f"syntax: {syntax}")
    # print(f"pass_val: {pass_val}")

    match_val = syntax.split()[1]
    first_pos = int(syntax.split()[0].split('-')[0]) - 1
    second_pos = int(syntax.split()[0].split('-')[1]) - 1
    print(f"Checking for occurences of {match_val} at positions {first_pos} or {second_pos}")
    
    # Exactly 1 should match, meaning we need an XOR
    if(bool(pass_val[first_pos] == match_val) != bool(pass_val[second_pos] == match_val)):
        print(f"{pass_val} is a valid password")
        valid_pass += 1

print(f"There are {valid_pass} valid passowrds")