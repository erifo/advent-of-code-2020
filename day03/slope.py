class Slope():
    def __init__(self, data):
        self.lines = data
        self.width = len(data[0])
        self.height = len(data)

    def get_char_at(self,x,y):
        line = self.lines[y]
        char = line[x % self.width]
        return char

    def is_tree(self,x,y):
        char = self.get_char_at(x,y)
        if char == "#":
            return True
        elif char == ".":
            return False
    
    def get_route(self, xmod, ymod):
        route = ""
        x = 0
        y = 0
        while (y < self.height):
            route += self.get_char_at(x,y)
            x += xmod
            y += ymod
        return route

    def trees_in_slope(self, xmod, ymod):
        route = self.get_route(xmod, ymod)
        return route.count("#")