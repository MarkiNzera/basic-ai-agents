from entities.agents.Agent import Agent
from entities.obstacles.Obstacle import Obstacle
from random import randint

print(Agent)

class SimpleReflexAgent(Agent):

    def __init__(self, name, symbol, initial_x, initial_y):
        super().__init__(name, symbol, initial_x, initial_y)

    def move(self, env):
        grid = env.grid

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        move = randint(0, 3)


        choosen_move = directions[move]
        agent_next_position = (self.pos[0] + choosen_move[0], self.pos[1] + choosen_move[1])
        
        if (self.is_valid_move(env, agent_next_position)):
            
            next_position = grid[agent_next_position[0]][agent_next_position[1]]
            self.collect_resource(next_position, env)

            if(next_position.is_base() and self.is_carrying_resource):
                self.deliver_resource()
            
            if(not next_position.is_obstacle()):
                self.pos = agent_next_position
        
        print(f"Moving {self.name} x={self.pos[0]} y={self.pos[1]} / Is Carrying resource={self.is_carrying_resource} / Score={self.score}")
        
        

