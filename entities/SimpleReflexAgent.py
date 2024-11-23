from entities.Agent import Agent
from random import randint

print(Agent)

class SimpleReflexAgent(Agent):

    def __init__(self, name, symbol, initial_x, initial_y):
        super().__init__(name, symbol, initial_x, initial_y)

    def move(self, grid):
        move = randint(0, 3)
        
        if (move == 0):
            self._move_up(grid)
        elif (move == 1):
            self._move_down(grid)
        elif (move == 2):
            self._move_left(grid)
        else:
            self._move_right(grid)

        print(f"Moving {self.name} x={self.x_pos} y={self.y_pos} / Is Carrying resource={self.is_carrying_resource} / Score={self.score}")

