import os

class Enviroment:

    def __init__(self, size, agents=[], obstacles=[], resources=[]):
        if len(agents) > 2:
            raise Exception("Maximum number of agents reached")

        self.agents = agents
        self.obstacles = obstacles
        self.resources = resources

        self.size = size
        self.update_grid()

    def add_agents(self, agent):
        if len(self.agents) >= 2:
            raise Exception("Maximum number of agents reached")
        self.agents.append(agent)

    def update_grid(self):
        self.grid = [["." for _ in range(self.size)] for _ in range(self.size)]
        self.grid[self.size//2][self.size//2] = "B"

        for obstacle in self.obstacles:
            self.grid[obstacle.y_pos][obstacle.x_pos] = obstacle.symbol

        for agent in self.agents:
            self.grid[agent.y_pos][agent.x_pos] = agent.symbol

        for resource in self.resources:
            self.grid[resource.y_pos][resource.x_pos] = resource.symbol

        self.print_grid()

    def print_grid(self):
        
        for row in self.grid:
            for pos in row:
                print(f"[{pos:^3}]", end="")
            print()

    def step(self):
        os.system("clear")
        for agent in self.agents:
            agent.move(self.grid)
        self.update_grid()
        