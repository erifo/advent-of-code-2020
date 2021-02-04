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
    return boot.accumulator

def solve_b(boot):
    for i in range(boot.length()):
        instr = boot.get_instr_at(i)
        if instr.type not in ["jmp", "nop"]:
            continue
        boot.jmpnop_switch_at(i)
        result = boot.run()
        if result == False: #Endless loop detected.
            boot.jmpnop_switch_at(i) #Switch back to original.
            continue
        if result == True:
            return boot.accumulator

def main():
    boot_a = load("data.txt")
    boot_b = load("data.txt")
    print("A:",solve_a(boot_a)) #1749
    print("B:",solve_b(boot_b)) #

main()