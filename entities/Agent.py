
class Agent:
    def __init__(self, name, symbol, initial_x, initial_y):
        self.name = name
        self.symbol = symbol
        self.x_pos = initial_x
        self.y_pos = initial_y

    def move(self, grid):
        pass

    def _move_down(self, grid_length):
        if (self.y_pos + 1 < grid_length):
            self.y_pos += 1
    
    def _move_up(self):
        if (self.y_pos - 1 >= 0):
            self.y_pos -= 1

    def _move_left(self):
        if (self.x_pos - 1 >= 0):
            self.x_pos -= 1

    def _move_right(self, grid_length):
        if (self.x_pos + 1 < grid_length):
            self.x_pos += 1
