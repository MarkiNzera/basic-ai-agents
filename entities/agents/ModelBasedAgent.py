from entities.agents.Agent import Agent
from collections import deque
from random import randint, shuffle, choice

class ModelBasedAgent(Agent):
    def __init__(self, name, symbol, initial_x, initial_y):
        super().__init__(name, symbol, initial_x, initial_y)
        self.table = [[[-1 for _ in range(11)] for _ in range(11)]]


    def move(self, env):
        grid = self.grid

        

    def choose_next_move(self):
        x, y = self.pos
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        shuffle(directions)

        for dx, dy in self.directions:
            next_position = (x + dx, y + dy)
            if self.is_valid_move(next_position) and self.table[next_position] != 1:
                return next_position
            
        while True:
            dx, dy = choice(directions)
            next_position = (x + dx, y + dy)
            if self.is_valid_move(next_position):
                return next_position

    def update_table(self, position):
        x, y = position
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            neighbor = (x + dx, y + dy)
            if self.is_valid_move(neighbor):
                self.table[neighbor] = self.grid[neighbor]
