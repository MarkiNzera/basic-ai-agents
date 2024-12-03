from entities.obstacles.Obstacle import Obstacle
from heapq import heappop, heappush
from collections import deque
from random import randint

class Agent:
    def __init__(self, name, symbol, initial_x, initial_y):
        self.name = name
        self.symbol = symbol
        self.pos = (initial_y, initial_x)
        self.is_carrying_resource = False
        self.score = 0
        self.loaded_resource = None

    def init(self, env):
        self.env = env

    def is_base(self):
        return False
    
    def is_resource(self):
        return False

    def is_obstacle(self):
        return True

    def is_free_space(self):
        return False

    def move(self):
        self._move_left(self.env)

    def print_status(self):
        print(f"Moving {self.name} x={self.pos[1]} y={self.pos[0]} / Is Carrying resource={self.is_carrying_resource} / Score={self.score}")


    def is_valid_move(self, position):
        x, y = position
        return (0 <= x < len(self.env.grid)) and (0 <= y < len(self.env.grid[0]))

    def collect_resource(self, resource):
        if (resource.is_resource() and self.is_carrying_resource):
            self.env.agents_shared_memory_of_resources_pos.append(resource.pos)

        if (resource.is_resource() and  not self.is_carrying_resource):
            if (resource in self.env.resources):
                self.is_carrying_resource = True
                self.loaded_resource = resource
                self.env.resources.remove(resource)
            self.env.grid[self.pos[0]][self.pos[1]] = Obstacle(".", self.pos[0], self.pos[1], False)
            return True
        return False

    def deliver_resource(self):
        self.is_carrying_resource = False
        self.score += self.loaded_resource.value

    def a_star(self, init, goal):
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

                    if self.is_carrying_resource:
                            
                        if self.is_valid_move(next_position) and (not self.env.grid[next_position[0]][next_position[1]].is_obstacle() or self.env.grid[next_position[0]][next_position[1]].is_base()) and next_position not in visited:
                            cost = len(path) + self.heuristic(next_position, goal)
                            heappush(pqueue, (cost, next_position, path))
                    else:

                        if self.is_valid_move(next_position) and (not self.env.grid[next_position[0]][next_position[1]].is_obstacle()) and next_position not in visited:
                            cost = len(path) + self.heuristic(next_position, goal)
                            heappush(pqueue, (cost, next_position, path))


        return []
    
    def heuristic(self, position, goal):
        x1, y1 = position
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2)
    
    def adjacent_is_resource(self):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        adjacent_positions = [(self.pos[0] + dx, self.pos[1] + dy) for dx, dy in directions]
        for adj_pos in adjacent_positions:
            if self.is_valid_move(adj_pos):
                cell = self.env.grid[adj_pos[0]][adj_pos[1]]
                if cell.is_resource() and not self.is_carrying_resource:
                    return adj_pos
            
        return None
    
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

    def __str__(self):
        return self.symbol
    
    def __format__(self, format_spec):
        return format(str(self), format_spec)