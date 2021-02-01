import re
from bags import Bag, ColorAmountPair

def load(filename):
    f = open(filename, "r")
    lines = f.readlines()
    bags = []
    for line in lines:
        outer_raw, inner_raw = line.split("contain")
        outer_color = re.search(r"^(\w+ \w+)", outer_raw.strip()).group(1)
        bag = Bag(outer_color)
        for inner in inner_raw.split(","):
            if re.search(r"no other bags.", inner.strip()):
                break
            inner_color = re.search(r"(\w+ \w+) bag[s]?", inner.strip()).group(1)
            amount = re.search(r"^(\d+) \w+ \w+", inner.strip()).group(1)
            bag.add_allowed_content(inner_color, int(amount))
        bags.append(bag)
    return bags

def print_bags(bags):
    for bag in bags:
        print("BAG:", bag.color)
        for allowed_content in bag.allowed_content:
            print("\tALLOWED:", allowed_content.amount, allowed_content.color)

def get_bag_with_color(bags, color):
    for bag in bags:
        if bag.color == color:
            return bag

def bag_leads_to_color(bags, bag, target_color):
    if bag.color == target_color:
        return True
    for allowed_content in bag.allowed_content:
        bag = get_bag_with_color(bags, allowed_content.color)
        if bag_leads_to_color(bags, bag, target_color):
            return True
    return False

def solve_a(data):
    count = 0
    target_color = "shiny gold"
    for bag in data:
        if bag.color == target_color:
            continue #Skip if our starting is gold.
        if bag_leads_to_color(data, bag, target_color):
            count += 1
    return count

def count_bags_inside_bag_with_color(bags, color):
    bag = get_bag_with_color(bags, color)
    total = 1
    for allowed_content in bag.allowed_content:
        for i in range(allowed_content.amount):
            total += count_bags_inside_bag_with_color(bags, allowed_content.color)
    return total

def solve_b(data):
    color = "shiny gold"
    return count_bags_inside_bag_with_color(data, color)-1 #Not counting the first bag.

def main():
    data = load("data.txt")
    print(solve_a(data)) #335
    print(solve_b(data)) #2431

main()