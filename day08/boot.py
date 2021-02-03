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
        instr.print()
        if (instr.called > 0):
            print("LOOP DETECTED")
            print("ACCUMULATOR:", self.accumulator)
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
    
    def run(self):
        while (True):
            instr = self.get_instr_at(self.position)
            if self.call(instr) == -1:
                break