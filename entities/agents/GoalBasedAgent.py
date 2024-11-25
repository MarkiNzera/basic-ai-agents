from entities.agents.Agent import Agent

class GoalBasedAgent(Agent):
    def __init__(self, name, symbol, initial_x, initial_y):
        super().__init__(name, symbol, initial_x, initial_y)

    def move(self, env):
        pass

    def set_goals(self, goals):
        self.goals = goals



