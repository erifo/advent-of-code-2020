import re

def search(regex, line):
    return re.search(regex, line).group(1)

def load(filename):
    f = open(filename, "r")
    lines = f.readlines()
    data = []
    for line in lines:
        entry = {}
        entry["first"] = int(search("^(\d+)-\d+", line))
        entry["second"] = int(search("^\d+-(\d+)", line))
        entry["letter"] = search("^\d+-\d+ (.):", line)
        entry["password"] = search("^\d+-\d+ .: (\w+)", line)
        data.append(entry)
    return data

def solve_a(data):
    nr_of_valid = 0
    for entry in data:
        pc = entry["password"].count(entry["letter"])
        if (pc >= entry["first"] and pc <= entry["second"]):
            nr_of_valid += 1
    return nr_of_valid

def solve_b(data):
    nr_of_valid = 0
    for entry in data:
        pw = entry["password"]
        ltr = entry["letter"]
        fst = entry["first"]
        snd = entry["second"]
        if pw[fst-1] == ltr and pw[snd-1] == ltr:
            continue
        if pw[fst-1] == ltr or pw[snd-1] == ltr:
            nr_of_valid += 1
    return nr_of_valid

def main():
    data = load("data.txt")
    print(solve_a(data)) #622
    print(solve_b(data)) #263

main()