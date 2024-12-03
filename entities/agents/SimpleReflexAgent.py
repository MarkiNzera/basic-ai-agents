from entities.agents.Agent import Agent

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
        
    