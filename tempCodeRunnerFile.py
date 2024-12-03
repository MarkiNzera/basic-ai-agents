
    agents=[simplesReflex1, simplesReflex2, simplesReflex3, goalBased1, modelBased1, utilityBased1],
    obstacles=obstacles,
    resources=resources
)

enviroment.init_agents()
while not enviroment.is_done():                                                                                                   
    sleep(0.5)                                                                                                    
    enviroment.step()

print(f"Done! Num of steps {enviroment.steps}")
for agent in enviroment.agents:
    print(f"Agente: {agent.name} Score: {agent.score}")
