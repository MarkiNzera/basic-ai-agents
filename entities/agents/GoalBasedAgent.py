from entities.agents.Agent import Agent
from heapq import heappop, heappush

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
            
            print(path)
            if path:
                next_path_position = path.pop(0)
                choosen_move = (next_path_position[0] - self.pos[0], next_path_position[1] - self.pos[1])
                agent_next_position = (self.pos[0] + choosen_move[0], self.pos[1] + choosen_move[1])
                next_position = grid[agent_next_position[0]][agent_next_position[1]]
                self.collect_resource(next_position, env)

                if(next_position.is_base() and self.is_carrying_resource):
                    self.deliver_resource()
                
                if(not next_position.is_obstacle()):
                    self.pos = agent_next_position

        print(f"Moving {self.name} x={self.pos[0]} y={self.pos[1]} / Is Carrying resource={self.is_carrying_resource} / Score={self.score}")

    def get_next_position(self):
        pass


    def return_to_base(self, env):
        return self.a_star(self.pos, (env.size//2, env.size//2), env)


    def go_to_resources(self, env):
        goal = env.resources[0]
        return self.a_star(self.pos, goal.pos, env)

    
    def a_star(self, init, goal, env):
        pqueue = []

        heappush(pqueue, (0, init, []))
        visited = set()

        while pqueue:
            priority, current_position, path = heappop(pqueue)

            if current_position not in visited:
                visited.add(current_position)

                path = path + [current_position]

                if current_position == goal:
                    path.pop(0)
                    return path

                x, y = current_position
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_position = (x + dx, y + dy)
                    if self.is_valid_move(env, next_position) and next_position not in visited:
                        cost = len(path) + self.heuristic(next_position, goal)
                        heappush(pqueue, (cost, next_position, path))

        return []

    def heuristic(self, position, goal):
        x1, y1 = position
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2)




