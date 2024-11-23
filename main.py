from time import sleep
from entities.Enviroment import Enviroment
from entities.agents.Agent import Agent
from entities.agents.SimpleReflexAgent import SimpleReflexAgent;
from entities.obstacles.Obstacle import Obstacle
from entities.obstacles.Resource import Resource

# agent1 = Agent("agent1", "A1", 10, 5)
agent2 = SimpleReflexAgent("Agente Reativo Simples", "A2", 6, 5)

obstacle1 = Obstacle("O", 2, 2, True)

resource1 = Resource("CE", 3, 3, 10)
resource2 = Resource("CE", 3, 6, 10)
resource3 = Resource("MR", 6, 3, 20)
resource4 = Resource("EA", 6, 6, 50)
resource5 = Resource("EA", 9, 5, 50)

enviroment = Enviroment(
    size=11, 
    agents=[agent2],
    obstacles=[obstacle1],
    resources=[resource1, resource2, resource3, resource4, resource5]
)

while not enviroment.is_done():
    # sleep(1)                                                                                                                     
    enviroment.step()

print(f"Done! Num of steps {enviroment.steps}")
for agent in enviroment.agents:
    print(f"Agent: {agent.name} Score: {agent.score}")
