from entities.agents.Agent import Agent
from entities.obstacles.Obstacle import Obstacle
from random import choice

print(Agent)

class SimpleReflexAgent(Agent):
    def _init_(self, name, symbol, initial_x, initial_y):
        super()._init_(name, symbol, initial_x, initial_y)
        self.returning_to_base = False

    def move(self):
        grid = self.env.grid
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        if self.is_carrying_resource:
            base_position = (self.env.size // 2, self.env.size // 2)
            path_to_base = self.a_star(self.pos, base_position)
            if path_to_base:
                next_step = path_to_base[0]
                self.pos = next_step
                if self.pos == base_position:
                    self.deliver_resource()
                    self.returning_to_base = False
        else:
            adjacent_positions = [(self.pos[0] + dx, self.pos[1] + dy) for dx, dy in directions]
            for adj_pos in adjacent_positions:
                if self.is_valid_move(adj_pos):
                    cell = grid[adj_pos[0]][adj_pos[1]]
                    if cell.is_resource():
                        self.collect_resource(cell)
                        return

            while True:
                move = choice(directions)
                agent_next_position = (self.pos[0] + move[0], self.pos[1] + move[1])
                if self.is_valid_move(agent_next_position):
                    next_position = grid[agent_next_position[0]][agent_next_position[1]]
                    if not next_position.is_obstacle():
                        self.pos = agent_next_position
                        break

        print(f"Moving {self.name} x={self.pos[0]} y={self.pos[1]} / Is Carrying resource={self.is_carrying_resource} / Score={self.score}")