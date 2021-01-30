import re
from slope import Slope

def load(filename):
    f = open(filename, "r")
    lines = f.readlines()
    data = [line.strip() for line in lines]
    return Slope(data)

def solve_a(data):
    return data.trees_in_slope(3,1)

def solve_b(data):
    routes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    answer = 1
    for route in routes:
        answer *= data.trees_in_slope(route[0], route[1])
    return answer


def main():
    data = load("data.txt")
    print(solve_a(data)) #232
    print(solve_b(data)) #3952291680

main()