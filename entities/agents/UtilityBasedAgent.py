from entities.agents.Agent import Agent

class UtilityBasedAgent(Agent):

    def __init__(self, name, symbol, initial_x, initial_y):
        super().__init__(name, symbol, initial_x, initial_y)

    def init(self, env):
        self.env = env
        self.utility_table = sorted(self.env.resources, reverse=True)

    def move(self):
        grid = self.env.grid
        
        if self.utility_table or self.is_carrying_resource:
            if self.is_carrying_resource:
                path = self.return_to_base()
            else:
                path = self.go_to_resources()
            
            if path:
                next_path_position = path.pop(0)
                next_position = grid[next_path_position[0]][next_path_position[1]]
                self.collect_resource(next_position)

                if(next_position.is_base() and self.is_carrying_resource):
                    self.utility_table.remove(self.loaded_resource)
                    self.deliver_resource()
                
                if(not next_position.is_obstacle()):
                    self.pos = next_path_position

            for resource in self.utility_table:
                print(resource, end=" ")
            print()
            print(path)



    def return_to_base(self):
        return self.a_star(self.pos, (self.env.size//2, self.env.size//2))

    def go_to_resources(self):
        goal = self.utility_table[0]
        return self.a_star(self.pos, goal.pos)