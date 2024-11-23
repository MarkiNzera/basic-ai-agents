from entities.Agent import Agent
from random import randint

print(Agent)

class SimpleReflexAgent(Agent):

    def __init__(self, name, symbol, initial_x, initial_y):
        super().__init__(name, symbol, initial_x, initial_y)

    def move(self, grid):
        grid_size = len(grid)

        move = randint(0, 3)
        
        if (move == 0):
            self._move_up()
        elif (move == 1):
            self._move_down(grid_size)
        elif (move == 2):
            self._move_left()
        else:
            self._move_right(grid_size)

        print(f"Moving {self.name} x={self.x_pos} y={self.y_pos}")

