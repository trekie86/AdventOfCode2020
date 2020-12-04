"""Advent of Code 2020 day 4 part 2"""
import re

required_keys = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def valid_passport(passport: map) -> bool:
    """Check if all of the conditions are met per passport field"""
    results = []
    results.append(validate_birth_year(passport))
    results.append(validate_issue_year(passport))
    results.append(validate_exp_year(passport))
    results.append(validate_height(passport))
    results.append(validate_hair_color(passport))
    results.append(validate_eye_color(passport))
    results.append(validate_passport_number(passport))

    return any(results) and all(results)

def validate_birth_year(passport: map) -> bool:
    """Validates the birth year field"""
    if passport.get('byr'):
        if int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002:
            return True

    return False

def validate_issue_year(passport: map) -> bool:
    """Validates the issue year field"""
    if passport.get('iyr'):
        if int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020:
            return True

    return False

def validate_exp_year(passport: map) -> bool:
    """Validates the expiration year field"""
    if passport.get('eyr'):
        if int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030:
            return True

    return False

def validate_height(passport: map) -> bool:
    """Validates the height field"""
    if passport.get('hgt'):
        if passport['hgt'].count('cm'):
            val = int(passport['hgt'][:passport['hgt'].find('cm')])
            if 150 <= val <= 193:
                return True
        elif passport['hgt'].count('in'):
            val = int(passport['hgt'][:passport['hgt'].find('in')])
            if 59 <= val <= 76:
                return True
        else:
            return False

    return False

def validate_hair_color(passport: map) -> bool:
    """Validates the hair color field"""
    if passport.get('hcl'):
        regex = re.compile('#[0-9a-f]{6}')
        match = regex.match(passport['hcl'])
        return bool(match)

    return False

def validate_eye_color(passport: map) -> bool:
    """Validates the eye color field"""
    if passport.get('ecl'):
        return passport['ecl'] in valid_eye_colors

    return False

def validate_passport_number(passport: map) -> bool:
    """Validate the passport number field"""
    if passport.get('pid'):
        return len(passport['pid']) == 9

    return False

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
