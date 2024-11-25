from entities.obstacles.Obstacle import Obstacle
from heapq import heappop, heappush

class Agent:
    def __init__(self, name, symbol, initial_x, initial_y):
        self.name = name
        self.symbol = symbol
        self.pos = (initial_y, initial_x)
        self.is_carrying_resource = False
        self.score = 0
        self.loaded_resource = None

    def is_base(self):
        return False
    
    def is_resource(self):
        return False

    def is_obstacle(self):
        return True

    def move(self, env):
        self._move_left(env)

        print(f"Moving {self.name} x={self.x_pos} y={self.y_pos} / Is Carrying resource={self.is_carrying_resource} / Score={self.score}")

    def is_valid_move(self, env, position):
        x, y = position
        return (0 <= x < len(env.grid)) and (0 <= y < len(env.grid[0]))

    def collect_resource(self, resource, env):
        if (resource.is_resource() and  not self.is_carrying_resource):
            self.is_carrying_resource = True
            self.loaded_resource = resource
            env.resources.remove(resource)
            env.grid[self.pos[0]][self.pos[1]] = Obstacle(".", self.pos[0], self.pos[1], False)

    def deliver_resource(self):
        self.is_carrying_resource = False
        self.score += self.loaded_resource.value

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

    def __str__(self):
        return self.symbol
    
    def __format__(self, format_spec):
        return format(str(self), format_spec)