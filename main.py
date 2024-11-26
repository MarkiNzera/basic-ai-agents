from time import sleep
from entities.Enviroment import Enviroment
from entities.agents.Agent import Agent
from entities.agents.SimpleReflexAgent import SimpleReflexAgent
from entities.agents.ModelBasedAgent import ModelBasedAgent
from entities.agents.GoalBasedAgent import GoalBasedAgent
from entities.agents.UtilityBasedAgent import UtilityBasedAgent
from entities.obstacles.Obstacle import Obstacle
from entities.obstacles.Resource import Resource

agent1 = SimpleReflexAgent("Reativo Simples 1", "A1", 4, 5)
agent2 = ModelBasedAgent("Baseado em Modelo 2", "A2", 6, 5)
agent3 = GoalBasedAgent("Baseado em Objetivo", "A3", 4, 5)
agent4 = UtilityBasedAgent("Baseado em Utilidade", "A4", 6, 5)

obstacle1 = Obstacle("O", 2, 2, True)

resource1 = Resource("CE", 3, 3, 10)
resource2 = Resource("CE", 3, 6, 10)
resource3 = Resource("MR", 6, 3, 20)
resource4 = Resource("EA", 9, 9, 50)
resource5 = Resource("EA", 1, 1, 50)

enviroment = Enviroment(
    size=11, 
    agents=[agent4],
    obstacles=[obstacle1],
    resources=[resource1, resource2, resource3, resource4, resource5]
)

enviroment.init_agents()
while not enviroment.is_done():
    sleep(0.1)                                                                                                                     
    enviroment.step()

print(f"Done! Num of steps {enviroment.steps}")
for agent in enviroment.agents:
    print(f"Agente: {agent.name} Score: {agent.score}")
