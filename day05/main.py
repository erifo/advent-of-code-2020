import re

def load(filename):
    f = open(filename, "r")
    lines = f.readlines()
    data = [line.strip() for line in lines]
    return data

def bp_to_id(bp):
    rows = [i for i in range(128)] #0...127
    columns = [i for i in range(8)] #0...7
    for char in bp:
        if char == "F":
            rows = rows[:len(rows)//2] #Lower
        elif char == "B":
            rows = rows[len(rows)//2:] #Upper
        elif char == "L":
            columns = columns[:len(columns)//2] #Lower
        elif char == "R":
            columns = columns[len(columns)//2:] #Upper
    return (rows[0] * 8) + columns[0]

def get_ids(bps):
    return [bp_to_id(bp) for bp in bps]

def get_highest_id(bps):
    return max(get_ids(bps))

def find_free_seat(ids):
    first = ids[0]
    last = ids[-1]
    for i in range(first,last):
        if i not in ids:
            return i

def solve_a(data):
    return get_highest_id(data)

def solve_b(data):
    ids = sorted(get_ids(data))
    return find_free_seat(ids)

def main():
    data = load("data.txt")
    print(solve_a(data)) #816
    print(solve_b(data)) #539

main()