from instruction import Instruction
from boot import Boot

def load(filename):
    f = open(filename, "r")
    lines = f.readlines()
    instructions = []
    for line in lines:
        instr_type, instr_val = line.split(" ")
        instr = Instruction(instr_type, int(instr_val))
        instructions.append(instr)
    return Boot(instructions)

def print_instructions(boot):
    for i in range(boot.length()):
        instr = boot.get_instr_at(i)
        print(i, ":", instr.type, instr.value)

def solve_a(boot):
    boot.run()

def solve_b(boot):
    pass

def main():
    boot = load("data.txt")
    print(solve_a(boot)) #1749
    print(solve_b(boot)) #

main()