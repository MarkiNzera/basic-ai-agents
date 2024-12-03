from entities.agents.Agent import Agent

class BDIAgent(Agent):
    def __init__(self, name, symbol, initial_x, initial_y):
        super().__init__(name, symbol, initial_x, initial_y)
        self.beliefs = {}
        self.desires = []
        self.intentions = []

    def perceive(self):
        self.beliefs['resources'] = sorted(self.env.resources, reverse=True)
        self.beliefs['position'] = self.pos 

    def deliberate(self):
        if self.is_carrying_resource:
            self.desires = ['return_to_base']
        else:
            self.desires = ['collect_resource']

    def plan(self):
        if 'return_to_base' in self.desires:
            self.intentions = self.a_star(self.pos, (self.env.size // 2, self.env.size // 2))
        elif 'collect_resource' in self.desires and self.beliefs['resources']:
            nearest_resource = self.beliefs['resources'][0]
            self.intentions = self.a_star(self.pos, nearest_resource.pos)

    def execute(self):
        if self.intentions:
            next_path_position = self.intentions.pop(0)
            next_position = self.env.grid[next_path_position[0]][next_path_position[1]]

            self.collect_resource(next_position)
            if next_position.is_base() and self.is_carrying_resource:
                self.deliver_resource()

            if not next_position.is_obstacle():
                self.pos = next_path_position
        

    def move(self):
        self.perceive() 
        self.deliberate()
        self.plan() 
        self.execute()