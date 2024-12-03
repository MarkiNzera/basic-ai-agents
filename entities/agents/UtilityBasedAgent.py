from entities.agents.Agent import Agent

class UtilityBasedAgent(Agent):

    def __init__(self, name, symbol, initial_x, initial_y):
        super().__init__(name, symbol, initial_x, initial_y)

    def init(self, env):
        self.env = env
        self.utility_table = sorted(self.env.resources, reverse=True)

    def move(self):
        grid = self.env.grid
        
        if self.is_carrying_resource:
            self.return_to_base()
            return
        
        # for agent in self.env.agents:
        #     if agent.is_needing_help:
        #         path = self.find_path_to_next_resource(agent.pos)
        #         if path:
        #             next_path_position = path.pop(0)
        #             next_position = grid[next_path_position[0]][next_path_position[1]]
        #             self.collect_resource(next_position)
        #             self.pos = next_path_position
        #             return
        
        if self.env.agents_shared_memory_of_resources:
            next_resource = max(self.env.agents_shared_memory_of_resources)
            path = self.find_path_to_next_resource(next_resource.pos)

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
