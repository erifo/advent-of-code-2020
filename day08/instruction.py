class Instruction():
    def __init__(self, instr_type, instr_val):
        self.type = instr_type
        self.value = instr_val
        self.called = 0
    
    def print(self):
        print("INSTR:", self.type, self.value, "CALLED:", self.called)