class ColorAmountPair():
    def __init__(self, color, amount):
        self.color = color
        self.amount = amount




class Bag():
    def __init__(self, color):
        self.color = color
        self.allowed_content = []

    def add_allowed_content(self, color, amount):
        ca_pair = ColorAmountPair(color, amount)
        self.allowed_content.append(ca_pair)