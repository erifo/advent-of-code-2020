class Boot():
    def __init__(self, instructions):
        self.instructions = instructions
        self.accumulator = 0
        self.position = 0

    def acc(self, amount):
        self.accumulator += amount
        self.position += 1

    def jmp(self, mod):
        self.position += mod 

    def nop(self):
        self.position += 1

    def call(self, instr):
        #instr.print()
        if (instr.called > 0):
            return -1
        instr.called += 1
        if instr.type == "acc":
            self.acc(instr.value)
        elif instr.type == "jmp":
            self.jmp(instr.value)
        elif (instr.type == "nop"):
            self.nop()
        return 0

    def length(self):
        return len(self.instructions)

    def get_instr_at(self, i):
        return self.instructions[i]
    
    def jmpnop_switch_at(self, i):
        instr = self.get_instr_at(i)
        #print("Switching instr [",instr.type,"] on line", i+1)
        if instr.type == "jmp":
            instr.type = "nop"
        elif instr.type == "nop":
            instr.type = "jmp"

    def run(self):
        while (self.position < self.length()):
            instr = self.get_instr_at(self.position)
            result = self.call(instr)
            if result == -1: #Endless loop detected.
                return False
        return True
        