from entities.agents.Agent import Agent
from collections import deque

class ModelBasedAgent(Agent):
    def __init__(self, name, symbol, initial_x, initial_y):
        super().__init__(name, symbol, initial_x, initial_y)
        self.visited = set()

    def move(self, env):
        pass


