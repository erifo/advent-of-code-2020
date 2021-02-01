import re

def load(filename):
    f = open(filename, "r")
    text = f.read()
    groups = []
    for lines in text.split("\n\n"):
        group = []
        for line in lines.split("\n"):
            group.append(line.strip())
        groups.append(group)
    return groups

def get_group_answer_set(group):
    answers = set()
    for person in group:
        for answer in person:
            answers.add(answer)
    return answers

def get_group_common_answer_set(group):
    answers = get_group_answer_set(group)
    common_answers = set()
    for answer in answers:
        common = True
        for person in group:
            if answer not in person:
                common = False
                break
        if common:
            common_answers.add(answer)
    return common_answers

def solve_a(data):
    answer_set_sum = 0
    for group in data:
        answer_set_sum += len(get_group_answer_set(group))
    return answer_set_sum

def solve_b(data):
    common_answer_set_sum = 0
    for group in data:
        common_answer_set_sum += len(get_group_common_answer_set(group))
    return common_answer_set_sum

def main():
    data = load("data.txt")
    print(solve_a(data)) #6565
    print(solve_b(data)) #3137

main()