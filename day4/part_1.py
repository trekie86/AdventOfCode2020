"""Advent of Code 2020 day 4 part 1"""

required_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_passport(passport: map) -> bool:
    """Check to ensure all of the keys in the passport map are in the required keys list"""
    return all(elem in passport.keys() for elem in required_keys)

def main():
    """The main function"""
    passport_list = []
    with open("day4/input.txt", "r") as f:
        passport = {}
        for line in f:
            if line.strip() == '':
                passport_list.append(passport)
                passport = {}
                continue
            whole_fields = line.split()
            for field in whole_fields:
                passport[field.split(':')[0]] = field.split(':')[1]
        passport_list.append(passport)

    # print(passport_list)

    valid = 0
    for passport in passport_list:
        if valid_passport(passport):
            # print(f"{passport} is valid")
            valid += 1

            # print(f"Invalid passport {passport}")

    print(f"{valid} valid passports out of {len(passport_list)}")

if __name__ == "__main__":
    # execute only if run as a script
    main()
