from entities.agents.Agent import Agent
from entities.obstacles.Obstacle import Obstacle
from random import randint

class SimpleReflexAgent(Agent):

    def __init__(self, name, symbol, initial_x, initial_y):
        super().__init__(name, symbol, initial_x, initial_y)

    def move(self):

        if self.is_carrying_resource:
            self.return_to_base()
            return

        pos = self.adjacent_is_resource()
        if (pos):
            next_position = self.env.grid[pos[0]][pos[1]]
            self.collect_resource(next_position)
            self.pos = pos
            return 
        
        self.choice_random_position()
        
        print(f"Moving {self.name} x={self.pos[0]} y={self.pos[1]} / Is Carrying resource={self.is_carrying_resource} / Score={self.score}")
        
    def find_path_to_base(self):
        return self.a_star(self.pos, (self.env.size//2, self.env.size//2))

    def return_to_base(self):
        path = self.find_path_to_base()
    
        if path:
            next_path_position = path.pop(0)
            next_position = self.env.grid[next_path_position[0]][next_path_position[1]]
            self.collect_resource(next_position)

            if(next_position.is_base() and self.is_carrying_resource):
                self.deliver_resource()
            
            if(not next_position.is_obstacle()):
                self.pos = next_path_position

    def choice_random_position(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        move = randint(0, 3)

        choosen_move = directions[move]
        agent_next_position = (self.pos[0] + choosen_move[0], self.pos[1] + choosen_move[1])
        
        if (self.is_valid_move(agent_next_position)):
            
            next_position = self.env.grid[agent_next_position[0]][agent_next_position[1]]
            self.collect_resource(next_position)

            if(next_position.is_base() and self.is_carrying_resource):
                self.deliver_resource()
            
            if(not next_position.is_obstacle()):
                self.pos = agent_next_position