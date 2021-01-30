import timeit

def load(filename):
    f = open(filename, "r")
    lines = f.readlines()
    return [int(line[:4]) for line in lines]

def solve_a(data):
    for i in range(len(data)):
        for j in range(len(data)):
            if (i == j):
                continue
            n1 = data[i]
            n2 = data[j]
            if n1 + n2 == 2020:
                return n1 * n2

def solve_b(data):
    for i in range(len(data)):
        for j in range(len(data)):
            for k in range(len(data)):
                if (i==j or i==k or j==k):
                    continue
                n1 = data[i]
                n2 = data[j]
                n3 = data[k]
                if n1 + n2 + n3 == 2020:
                    return n1 * n2 * n3

def main():
    data = load("data.txt")
    print(solve_a(data)) #121396
    print(solve_b(data)) #73616634

main()