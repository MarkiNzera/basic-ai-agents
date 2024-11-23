from entities.obstacles.Obstacle import Obstacle

class Agent:
    def __init__(self, name, symbol, initial_x, initial_y):
        self.name = name
        self.symbol = symbol
        self.x_pos = initial_x
        self.y_pos = initial_y
        self.is_carrying_resource = False
        self.score = 0
        self.loaded_resource = None

    def is_base(self):
        return True
    
    def is_resource(self):
        return False

    def is_obstacle(self):
        return True

    def move(self, env):
        self._move_left(env)

        print(f"Moving {self.name} x={self.x_pos} y={self.y_pos} / Is Carrying resource={self.is_carrying_resource} / Score={self.score}")

    def _move_down(self, env):
        grid = env.grid
        if (self.y_pos + 1 < len(grid)):
            if (grid[self.y_pos + 1][self.x_pos].is_resource() and not self.is_carrying_resource):
                self.collect_resource(grid[self.y_pos + 1][self.x_pos])
                env.resources.remove(grid[self.y_pos + 1][self.x_pos])
                grid[self.y_pos + 1][self.x_pos] = Obstacle(".", self.y_pos + 1, self.x_pos, False)
            
            if (grid[self.y_pos + 1][self.x_pos].is_base() and self.is_carrying_resource):
                self.deliver_resource()
                return
            
            if (grid[self.y_pos + 1][self.x_pos].is_obstacle()):
                return

            self.y_pos += 1
    
    def _move_up(self, env):
        grid = env.grid
        if (self.y_pos - 1 >= 0):
            if (grid[self.y_pos - 1][self.x_pos].is_resource() and not self.is_carrying_resource):
                self.collect_resource(grid[self.y_pos - 1][self.x_pos])
                env.resources.remove(grid[self.y_pos - 1][self.x_pos])
                grid[self.y_pos - 1][self.x_pos] = Obstacle(".", self.y_pos - 1, self.x_pos, False)

            if (grid[self.y_pos - 1][self.x_pos].is_base() and self.is_carrying_resource):
                self.deliver_resource()
                return
            
            if (grid[self.y_pos - 1][self.x_pos].is_obstacle()):
                return

            self.y_pos -= 1

    def _move_left(self, env):
        grid = env.grid
        if (self.x_pos - 1 >= 0):
            if (grid[self.y_pos][self.x_pos - 1].is_resource() and not self.is_carrying_resource):
                self.collect_resource(grid[self.y_pos][self.x_pos - 1])
                env.resources.remove(grid[self.y_pos][self.x_pos - 1])
                grid[self.y_pos][self.x_pos - 1] = Obstacle(".", self.y_pos, self.x_pos - 1, False)
        
            if (grid[self.y_pos][self.x_pos - 1].is_base() and self.is_carrying_resource):
                self.deliver_resource()
                return
            
            if (grid[self.y_pos][self.x_pos - 1].is_obstacle()):
                return

            self.x_pos -= 1

    def _move_right(self, env):
        grid = env.grid
        if (self.x_pos + 1 < len(grid)):
            if (grid[self.y_pos][self.x_pos + 1].is_resource() and not self.is_carrying_resource):
                self.collect_resource(grid[self.y_pos][self.x_pos + 1])
                env.resources.remove(grid[self.y_pos][self.x_pos + 1])
                grid[self.y_pos][self.x_pos + 1] = Obstacle(".", self.y_pos, self.x_pos + 1, False)
        
            if (grid[self.y_pos][self.x_pos + 1].is_base() and self.is_carrying_resource):
                self.deliver_resource()
                return
            
            if (grid[self.y_pos][self.x_pos + 1].is_obstacle()):
                return

            self.x_pos += 1

    def collect_resource(self, resource):
        self.is_carrying_resource = True
        self.loaded_resource = resource

    def deliver_resource(self):
        self.is_carrying_resource = False
        self.score += self.loaded_resource.value

    def __str__(self):
        return self.symbol
    
    def __format__(self, format_spec):
        return format(str(self), format_spec)