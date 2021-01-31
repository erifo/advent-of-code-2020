import re

def load(filename):
    f = open(filename, "r")
    text = f.read()
    data = text.split("\n\n")
    data = [entry.replace("\n", " ").strip() for entry in data]
    return data

def process_data(data):
    passports = []
    for entry in data:
        passport = {}
        for field in entry.split(' '):
            keyval = field.split(':')
            passport[keyval[0]] = keyval[1]
        passports.append(passport)
    return passports

def are_fields_in_passport(fields, passport):
    for field in fields:
        if not field in passport:
            return False
    return True

def solve_a(data):
    fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = 0
    for passport in data:
        if not are_fields_in_passport(fields, passport):
            continue        
        valid += 1
    return valid

# ---

def is_field_valid(passport, field, policy_regex):
    if field not in passport:
        return False
    if not re.search(policy_regex, passport[field]):
        return False
    return True

def are_fields_valid(passport, policy):
    for field, regex in policy.items():
        if not is_field_valid(passport, field, regex):
            return False
    return True

def solve_b(data):
    policy = {
        "byr": r"^(19[2-9][0-9]|200[0-2])$",
        "iyr": r"^(201[0-9]|2020)$",
        "eyr": r"^(202[0-9]|2030)$",
        "hgt": r"^(((1[5-8][0-9]|19[0-3])cm)|((59|6[0-9]|7[0-6])in))$",
        "hcl": r"^#[0-9|a-f]{6}$",
        "ecl": r"^(amb|blu|brn|gry|grn|hzl|oth)$",
        "pid": r"^\d{9}$"
    }
    valid = 0
    for passport in data:
        if not are_fields_valid(passport, policy):
            continue
        print("VALID:", sorted(passport.items(), reverse=True))
        valid += 1
    return valid

def main():
    data = load("data.txt")
    data = process_data(data) 
    print(solve_a(data)) #219
    print(solve_b(data)) #127

main()