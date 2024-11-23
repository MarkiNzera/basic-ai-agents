
class Obstacle:
    def __init__(self, symbol, initial_x, initial_y):
        self.x_pos = initial_x
        self.y_pos = initial_y
        self.symbol = symbol

    def is_obstable(self):
        return True
