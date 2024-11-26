from entities.agents.Agent import Agent

class ModelBasedAgent(Agent):
    def __init__(self, name, symbol, initial_x, initial_y):
        super().__init__(name, symbol, initial_x, initial_y)

    def move(self):
        grid = self.env.grid

        if self.is_carrying_resource:
            path = self.return_to_base()
        else:
            path = self.find_next_resource()
        
        if path:
            next_path_position = path.pop(0)
            next_position = grid[next_path_position[0]][next_path_position[1]]
            self.collect_resource(next_position)

            if(next_position.is_base() and self.is_carrying_resource):
                self.deliver_resource()
            
            if(not next_position.is_obstacle()):
                self.pos = next_path_position
        
        print(f"Moving {self.name} x={self.pos[0]} y={self.pos[1]} / Is Carrying resource={self.is_carrying_resource} / Score={self.score}")

    def find_next_resource(self):
        return self.bsf()

    def return_to_base(self):
        return self.a_star(self.pos, (self.env.size//2, self.env.size//2))