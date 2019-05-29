import random
import string
from Agent import Agent
from fuzzywuzzy import fuzz

user_string = input("Enter in the string you want to be guessed :")
length = len(user_string)
population_size = 100

def generate_population( ):
    agent_array = [Agent(length) for i in range(population_size)]
    return agent_array
def fitness(agentArray,inputString):
    count = 0
    for i in agentArray:
        agent = agentArray[count]
        agent_string = agent.string
        count+=1
        agent.fitness = fuzz.ratio(agent_string,inputString)
       # print(agent.string + " " +str(agent.fitness))
def selection(agentArray):
    agentArray.sort(key=lambda x: x.fitness , reverse = True)
    print(agentArray[0].string + " " + str(agentArray[0].fitness))
    print(agentArray[1].string + " " + str(agentArray[1].fitness))

    return [agentArray[0] + agentArray[1]]




def main():
    print("in main")
    #initial population
    agent_array = generate_population()
    fitness(agent_array,user_string)
    breeding_pairs = selection(agent_array)



    #crossover

    #mutation








main()










