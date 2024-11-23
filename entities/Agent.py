
class Agent:
    def __init__(self, name, symbol, initial_x, initial_y):
        self.name = name
        self.symbol = symbol
        self.x_pos = initial_x
        self.y_pos = initial_y

    def is_obstacle(self):
        return True

    def move(self, grid):
        pass

    def _move_down(self, grid):
        if (grid[self.y_pos + 1][self.x_pos].is_obstacle()):
            return
        if (self.y_pos + 1 < len(grid)):
            self.y_pos += 1
    
    def _move_up(self, grid):
        if (grid[self.y_pos - 1][self.x_pos].is_obstacle()):
            return

        if (self.y_pos - 1 >= 0):
            self.y_pos -= 1

    def _move_left(self, grid):
        if (grid[self.y_pos][self.x_pos - 1].is_obstacle()):
            return
        
        if (self.x_pos - 1 >= 0):
            self.x_pos -= 1

    def _move_right(self, grid):
        if (grid[self.y_pos][self.x_pos + 1].is_obstacle()):
            return
        
        if (self.x_pos + 1 < len(grid)):
            self.x_pos += 1

    def __str__(self):
        return self.symbol
    
    def __format__(self, format_spec):
        return format(str(self), format_spec)