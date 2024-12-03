from entities.obstacles.Obstacle import Obstacle
from heapq import heappop, heappush
from collections import deque


class Agent:
    def _init_(self, name, symbol, initial_x, initial_y):
        self.name = name
        self.symbol = symbol
        self.pos = (initial_y, initial_x)
        self.is_carrying_resource = False
        self.score = 0
        self.loaded_resource = None
        self.waiting_for_resource= False

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

        print(f"Moving {self.name} x={self.x_pos} y={self.y_pos} / Is Carrying resource={self.is_carrying_resource} / Score={self.score}")

    def is_valid_move(self, position):
        x, y = position
        return (0 <= x < len(self.env.grid)) and (0 <= y < len(self.env.grid[0]))

    def collect_resource(self, resource):
        if (resource.is_resource() and  not self.is_carrying_resource):
            if(resource.value==50):
                resource.agents_at_resource.add(self)
                if len(resource.agents_at_resource) > 1:
                    self.waiting_for_resource = False
                    self.is_carrying_resource = True
                    self.loaded_resource = resource
                    self.env.resources.remove(resource)
                    self.env.grid[self.pos[0]][self.pos[1]] = Obstacle(".", self.pos[0], self.pos[1], False)
                    resource.agents_at_resource.clear()
                    print(f"{self.name} coletou o recurso de valor 50 com ajuda de outro agente.")
                    return True
                else:
                    print(f"{self.name} está esperando no recurso de valor 50.")
                    self.waiting_for_resource = True
                    return False
            else:
                if resource in self.env.resources:
                    self.is_carrying_resource = True
                    self.loaded_resource = resource
                    self.env.resources.remove(resource)
                self.env.grid[self.pos[0]][self.pos[1]] = Obstacle(".", self.pos[0], self.pos[1], False)
                self.waiting_for_resource = False
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

    def _str_(self):
        return self.symbol
    
    def _format_(self, format_spec):
        return format(str(self), format_spec)


from entities.agents.Agent import Agent
from random import randint

class ModelBasedAgent(Agent):
    def _init_(self, name, symbol, initial_x, initial_y):
        super()._init_(name, symbol, initial_x, initial_y)

        self.memo_visited_pos = set()
        self.memo_resources = set()
        self.waiting_for_resource = False

    def move(self):
        grid = self.env.grid

        if self.is_carrying_resource:
            self.return_to_base()
            return
        
        if self.waiting_for_resource:
                resource_pos = self.adjacent_is_resource()
                if resource_pos:
                    resource = self.env.grid[resource_pos[0]][resource_pos[1]]
                    if resource not in self.env.resources:
                        self.waiting_for_resource = False
                        print(f"{self.name} detectou que o recurso foi coletado, voltando a se mover.")
                    else:
                        print(f"{self.name} ainda está esperando no recurso.")
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
            if not self.collect_resource(next_position):
                self.waiting_for_resource = True
            else:
                self.waiting_for_resource = False
                self.pos = pos
                self.memo_visited_pos.add(self.pos)
            return 

        self.choice_random_position()
        
        print(f"Moving {self.name} x={self.pos[0]} y={self.pos[1]} / Is Carrying resource={self.is_carrying_resource} / Score={self.score}")

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
        move = randint(0, 3)

        choosen_move = directions[move]
        agent_next_position = (self.pos[0] + choosen_move[0], self.pos[1] + choosen_move[1])
        
        if (self.is_valid_move(agent_next_position) and agent_next_position not in self.memo_visited_pos):
            
            next_position = self.env.grid[agent_next_position[0]][agent_next_position[1]]
            self.collect_resource(next_position)

            if(next_position.is_base() and self.is_carrying_resource):
                self.deliver_resource()
            
            if(not next_position.is_obstacle()):
                self.pos = agent_next_position

            return

    def find_path_to_next_resource(self, resource_pos):
        return self.a_star(self.pos, resource_pos)
    
    def collect_resource(self, resource):
        if (self.is_carrying_resource and resource.is_resource()):
            self.memo_resources.add(resource.pos)
        if super().collect_resource(resource) and resource.pos in self.memo_resources:
            self.memo_resources.remove(resource.pos)


class Resource:

    def _init_(self, symbol, initial_x, initial_y, value):
        self.pos = (initial_y, initial_x)
        self.symbol = symbol
        self.collected = False
        self.value = value
        self.agents_at_resource = set()

    def value(self):
        return self.value

    def is_base(self):
        return False

    def is_resource(self):
        return True

    def is_obstacle(self):
        return False
    
    def is_free_space(self):
        return False

    def _str_(self):
        return self.symbol

    def _format_(self, format_spec):
        return format(str(self), format_spec)
    
    def _lt_(self, other):
        return self.value < other.value
    

for agent in self.env.agents:
    if agent.is_needing_help:
        path = self.find_path_to_next_resource(agent.pos)
        if path:
            next_path_position = path.pop(0)
            next_position = grid[next_path_position[0]][next_path_position[1]]
            self.collect_resource(next_position)
            self.pos = next_path_position
            return