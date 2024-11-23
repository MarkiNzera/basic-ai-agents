
class Resource:

    def __init__(self, symbol, initial_x, initial_y, value):
        self.x_pos = initial_x
        self.y_pos = initial_y
        self.symbol = symbol
        self.collected = False
        self.value = value

    def is_base(self):
        return False

    def is_resource(self):
        return True

    def is_obstacle(self):
        return False

    def __str__(self):
        return self.symbol

    def __format__(self, format_spec):
        return format(str(self), format_spec)