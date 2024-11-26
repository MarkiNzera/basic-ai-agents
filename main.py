from time import sleep
from random import randint
from entities.Enviroment import Enviroment
from entities.agents.Agent import Agent
from entities.agents.SimpleReflexAgent import SimpleReflexAgent
from entities.agents.ModelBasedAgent import ModelBasedAgent
from entities.agents.GoalBasedAgent import GoalBasedAgent
from entities.agents.UtilityBasedAgent import UtilityBasedAgent
from entities.obstacles.Obstacle import Obstacle
from entities.obstacles.Resource import Resource

grid_size = 101

agent1_initial_pos = (grid_size//2 - 1, grid_size//2)
agent2_initial_pos = (grid_size//2 + 1, grid_size//2)

simplesReflex1 = SimpleReflexAgent("Reativo Simples 1", "SR1", agent1_initial_pos[0], agent1_initial_pos[1])
simplesReflex2 = SimpleReflexAgent("Reativo Simples 2", "SR2", agent2_initial_pos[0], agent2_initial_pos[1])

modelBased1 = ModelBasedAgent("Baseado em Modelo 1", "MB1", agent1_initial_pos[0], agent1_initial_pos[1])
modelBased2 = ModelBasedAgent("Baseado em Modelo 2", "MB2", agent2_initial_pos[0], agent2_initial_pos[1])

goalBased1 = GoalBasedAgent("Baseado em Objetivo", "GB1", agent1_initial_pos[0], agent1_initial_pos[1])
goalBased2 = GoalBasedAgent("Baseado em Objetivo", "GB2", agent2_initial_pos[0], agent2_initial_pos[1])

utilityBased1 = UtilityBasedAgent("Baseado em Utilidade 1", "UB1", agent1_initial_pos[0], agent1_initial_pos[1])
utilityBased2 = UtilityBasedAgent("Baseado em Utilidade 2", "UB2", agent2_initial_pos[0], agent2_initial_pos[1])

grid_ocupied_spaces = [(grid_size//2, grid_size//2), agent1_initial_pos, agent2_initial_pos]


obstacles = []
for i in range(10):
    pos = (randint(0, grid_size - 1), randint(0, grid_size - 1))
    if pos not in grid_ocupied_spaces:
        obstacles.append(Obstacle("O", pos[0], pos[1], True))
        grid_ocupied_spaces.append(pos)

resources = []

for i in range(4):
    pos = (randint(0, grid_size - 1), randint(0, grid_size - 1))
    if pos not in grid_ocupied_spaces:
        resources.append(Resource("CE", pos[0], pos[1], 10))
        grid_ocupied_spaces.append(pos)

for i in range(3):
    pos = (randint(0, grid_size - 1), randint(0, grid_size - 1))
    if pos not in grid_ocupied_spaces:
        resources.append(Resource("MR", pos[0], pos[1], 20))
        grid_ocupied_spaces.append(pos)

for i in range(2):
    pos = (randint(0, grid_size - 1), randint(0, grid_size - 1))
    if pos not in grid_ocupied_spaces:
        resources.append(Resource("EA", pos[0], pos[1], 50))
        grid_ocupied_spaces.append(pos)

enviroment = Enviroment(
    size=grid_size, 
    agents=[goalBased1],
    obstacles=obstacles,
    resources=resources
)

enviroment.init_agents()
while not enviroment.is_done():                                                                                                   
    # sleep(1)                                                                                                                     
    enviroment.step()

print(f"Done! Num of steps {enviroment.steps}")
for agent in enviroment.agents:
    print(f"Agente: {agent.name} Score: {agent.score}")
