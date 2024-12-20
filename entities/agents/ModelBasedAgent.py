from entities.agents.Agent import Agent
from random import choice

class ModelBasedAgent(Agent):
    def __init__(self, name, symbol, initial_x, initial_y):
        super().__init__(name, symbol, initial_x, initial_y)

        self.memo_visited_pos = set()
        self.memo_resources = set()

    def move(self):
        grid = self.env.grid
        
        self.env.agents_shared_memory_of_resources += self.save_all_adjacents()
        if self.is_carrying_resource:
            self.return_to_base()
            return
        
        if self.memo_resources:
            path = self.find_path_to_next_resource(list(self.memo_resources)[0])
            if path:
                next_path_position = path.pop(0)
                next_position = grid[next_path_position[0]][next_path_position[1]]
                self.collect_resource(next_position)
                self.pos = next_path_position
                self.memo_visited_pos.add(self.pos)
                return
        
        pos = self.adjacent_is_resource()
        if (pos):
            next_position = self.env.grid[pos[0]][pos[1]]
            self.collect_resource(next_position)
            self.pos = pos
            self.memo_visited_pos.add(self.pos)
            return 

        self.choice_random_position()

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
                self.memo_visited_pos.add(self.pos)

    def choice_random_position(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        possible_moves = []
        for direction in directions:
            next_position = (self.pos[0] + direction[0], self.pos[1] + direction[1])
            if self.is_valid_move(next_position) and next_position not in self.memo_visited_pos:
                possible_moves.append(next_position)

        if possible_moves:
            agent_next_position = choice(possible_moves)
        else:
            choosen_move = choice(directions)
            agent_next_position = (self.pos[0] + choosen_move[0], self.pos[1] + choosen_move[1])
            if not self.is_valid_move(agent_next_position):
                return

        next_position = self.env.grid[agent_next_position[0]][agent_next_position[1]]
        self.collect_resource(next_position)

        if(next_position.is_base() and self.is_carrying_resource):
            self.deliver_resource()
        
        if(not next_position.is_obstacle()):
            self.pos = agent_next_position

        self.memo_visited_pos.add(agent_next_position)
    
    def collect_resource(self, resource):
        if (self.is_carrying_resource and resource.is_resource()):
            self.memo_resources.add(resource.pos)
        if super().collect_resource(resource) and resource.pos in self.memo_resources:
            self.memo_resources.remove(resource.pos)