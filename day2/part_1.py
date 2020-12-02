"""Advent of Code 2020 day 2 part 1"""

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
    min_count = int(syntax.split()[0].split('-')[0])
    max_count = int(syntax.split()[0].split('-')[1])
    print(f"Checking for occurences of {match_val} with a min/max of {min_count}/{max_count}")

    num_occurs = pass_val.count(match_val)
    # print(f"Found {num_occurs} {match_val} in {pass_val}")
    if(min_count <= num_occurs and max_count >= num_occurs):
        print(f"{pass_val} is a valid password")
        valid_pass += 1

print(f"There are {valid_pass} valid passowrds")