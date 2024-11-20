from time import sleep
from entities.Enviroment import Enviroment
from entities.Agent import Agent

agent1 = Agent("agent1", "A1", 4, 5)
agent2 = Agent("agent2", "A2", 6, 5)

enviroment = Enviroment(size=11, agents=[agent1, agent2])

while True:
    enviroment.step()
    sleep(1)                                                                                                                     
