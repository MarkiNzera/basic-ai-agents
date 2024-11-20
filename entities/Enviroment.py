import os

class Enviroment:

    def __init__(self, size, agents=[]):
        self.size = size
        self.agents = agents
        self.update_grid()

    def add_agents(self, agent):
        if len(self.agents) >= 2:
            raise Exception("Maximum number of agents reached")
        self.agents.append(agent)

    def update_grid(self):
        self.grid = [["." for _ in range(self.size)] for _ in range(self.size)]
        self.grid[self.size//2][self.size//2] = "B"
        for agent in self.agents:
            self.grid[agent.y_pos][agent.x_pos] = agent.symbol

    def print_grid(self):
        for row in self.grid:
            for pos in row:
                print(f"[{pos:^3}]", end="")
            print()

    def step(self):
        os.system("clear")
        self.update_grid()
        self.print_grid()
        for agent in self.agents:
            agent.move(self.grid)