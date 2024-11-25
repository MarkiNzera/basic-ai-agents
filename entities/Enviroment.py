import os
from entities.obstacles.Obstacle import Obstacle
from entities.obstacles.Base import Base

class Enviroment:

    def __init__(self, size, agents=[], obstacles=[], resources=[]):
        if len(agents) > 2:
            raise Exception("Maximum number of agents reached")

        self.agents = agents
        self.obstacles = obstacles
        self.resources = resources

        self.size = size
        self.update_grid()

        self.steps = 0

    def add_agents(self, agent):
        if len(self.agents) >= 2:
            raise Exception("Maximum number of agents reached")
        self.agents.append(agent)

    def update_grid(self):
        self.grid = [[Obstacle(".", j, i, False) for i in range(self.size)] for j in range(self.size)]
        self.grid[self.size//2][self.size//2] = Base(self.size//2, self.size//2)

        for obstacle in self.obstacles:
            self.grid[obstacle.y_pos][obstacle.x_pos] = obstacle

        for agent in self.agents:
            self.grid[agent.pos[0]][agent.pos[1]] = agent

        for resource in self.resources:
            self.grid[resource.pos[0]][resource.pos[1]] = resource

        self.print_grid()

    def print_grid(self):
        
        for row in self.grid:
            for pos in row:
                print(f"[{pos:^3}]", end="")
            print()

    def step(self):
        os.system("clear")
        for agent in self.agents:
            agent.move(self)
        self.steps += 1
        print(f"step: {self.steps}")
        self.update_grid()
        
    def is_done(self):
        for agent in self.agents:
            if agent.is_carrying_resource:
                return False

        return len(self.resources) == 0
    