
class Resource:

    def __init__(self, symbol, initial_x, initial_y, value):
        self.x_pos = initial_x
        self.y_pos = initial_y
        self.symbol = symbol
        self.collected = False
        self.value = value
