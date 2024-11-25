from entities.agents.Agent import Agent

class GoalBasedAgent(Agent):
    def __init__(self, name, symbol, initial_x, initial_y):
        super().__init__(name, symbol, initial_x, initial_y)

    def move(self, env):
        resources = env.resources
        grid = env.grid
        
        if resources or self.is_carrying_resource:
            if self.is_carrying_resource:
                path = self.return_to_base(env)
            else:
                path = self.go_to_resources(env)
            
            if path:
                next_path_position = path.pop(0)
                next_position = grid[next_path_position[0]][next_path_position[1]]
                self.collect_resource(next_position, env)

                if(next_position.is_base() and self.is_carrying_resource):
                    self.deliver_resource()
                
                if(not next_position.is_obstacle()):
                    self.pos = next_path_position

        print(f"Moving {self.name} x={self.pos[0]} y={self.pos[1]} / Is Carrying resource={self.is_carrying_resource} / Score={self.score}")

    def get_next_position(self):
        pass


    def return_to_base(self, env):
        return self.a_star(self.pos, (env.size//2, env.size//2), env)


    def go_to_resources(self, env):
        goal = env.resources[0]
        return self.a_star(self.pos, goal.pos, env)


    def heuristic(self, position, goal):
        x1, y1 = position
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2)




