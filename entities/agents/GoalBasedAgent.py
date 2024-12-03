from entities.agents.Agent import Agent

class GoalBasedAgent(Agent):
    def __init__(self, name, symbol, initial_x, initial_y):
        super().__init__(name, symbol, initial_x, initial_y)


    def move(self,):
        grid = self.env.grid
        
        if self.is_carrying_resource:
            self.return_to_base()
            return
        
        if self.env.agents_shared_memory_of_resources_pos:
            path = self.find_path_to_next_resource(self.env.agents_shared_memory_of_resources_pos[0])
            if path:
                next_path_position = path.pop(0)
                next_position = grid[next_path_position[0]][next_path_position[1]]
                self.collect_resource(next_position)
                self.pos = next_path_position
                return
        
        pos = self.adjacent_is_resource()
        if (pos):
            next_position = self.env.grid[pos[0]][pos[1]]
            self.collect_resource(next_position)
            self.pos = pos
            return 

        self.choice_random_position()







