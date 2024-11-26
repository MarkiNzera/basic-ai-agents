
class Resource:

    def __init__(self, symbol, initial_x, initial_y, value):
        self.pos = (initial_y, initial_x)
        self.symbol = symbol
        self.collected = False
        self.value = value

    def is_base(self):
        return False

    def is_resource(self):
        return True

    def is_obstacle(self):
        return False
    
    def is_free_space(self):
        return False

    def __str__(self):
        return self.symbol

    def __format__(self, format_spec):
        return format(str(self), format_spec)
    
    def __lt__(self, other):
        return self.value < other.value