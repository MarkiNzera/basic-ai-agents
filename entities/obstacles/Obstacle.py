
class Obstacle:
    def __init__(self, symbol, initial_x, initial_y, is_obstacle):
        self.x_pos = initial_x
        self.y_pos = initial_y
        self.symbol = symbol
        self._is_obstacle = is_obstacle

    def is_base(self):
        return False

    def is_resource(self):
        return False

    def is_obstacle(self):
        return self._is_obstacle

    def __str__(self):
        return f"{self.symbol}"
    
    def __format__(self, format_spec):
        return format(str(self), format_spec)