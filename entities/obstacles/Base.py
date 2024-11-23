
class Base:
    def __init__(self, initial_x, initial_y):
        self.x_pos = initial_x
        self.y_pos = initial_y
        self.symbol = "B"

    def is_obstacle(self):
        return True

    def __str__(self):
        return f"{self.symbol}"
    
    def __format__(self, format_spec):
        return format(str(self), format_spec)
