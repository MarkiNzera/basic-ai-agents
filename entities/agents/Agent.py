from entities.obstacles.Obstacle import Obstacle
from heapq import heappop, heappush
from collections import deque

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

        print(f"Moving {self.name} x={self.x_pos} y={self.y_pos} / Is Carrying resource={self.is_carrying_resource} / Score={self.score}")

    def is_valid_move(self, position):
        x, y = position
        return (0 <= x < len(self.env.grid)) and (0 <= y < len(self.env.grid[0]))

    def collect_resource(self, resource):
        if (resource.is_resource() and  not self.is_carrying_resource):
            if (resource in self.env.resources):
                self.is_carrying_resource = True
                self.loaded_resource = resource
                self.env.resources.remove(resource)
            self.env.grid[self.pos[0]][self.pos[1]] = Obstacle(".", self.pos[0], self.pos[1], False)

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

                    if self.is_valid_move(next_position) and not self.env.grid[next_position[0]][next_position[1]].is_obstacle() and next_position not in visited:
                        cost = len(path) + self.heuristic(next_position, goal)
                        heappush(pqueue, (cost, next_position, path))

        return []
    
    def heuristic(self, position, goal):
        x1, y1 = position
        x2, y2 = goal
        return abs(x1 - x2) + abs(y1 - y2)

    def bsf(self):
        queue = deque([(self.pos, [self.pos])])
        visited = set()
        
        while queue:
            (x, y), path = queue.popleft()
            if not (x, y) in visited:
                visited.add((x, y))

                if (self.env.grid[x][y].is_resource()):
                    path.pop(0)
                    return path
                
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    next_position = (x + dx, y + dy)
                    if self.is_valid_move(next_position) and not self.env.grid[next_position[0]][next_position[1]].is_obstacle() and next_position not in visited:
                        queue.append((next_position, path + [next_position]))
        return []

    def __str__(self):
        return self.symbol
    
    def __format__(self, format_spec):
        return format(str(self), format_spec)