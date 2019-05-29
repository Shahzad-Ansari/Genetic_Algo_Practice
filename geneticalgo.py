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
    breedingPairs = [agentArray[0] , agentArray[1]]
    return breedingPairs
def crossover(breedingPairs):
    random_num = random.randint(0,length)
    breedingPair1 = breedingPairs[0].string
    breedingPair2 = breedingPairs[1].string

    crossover_array1 = []
    crossover_array2 = []
    crossover_array3 = []
    crossover_array4 = []
    count = 0
    for i in range(length):
        if count <= random_num:
            crossover_array1.append(breedingPair1[count])
            crossover_array2.append(breedingPair2[count])
            count+=1
        else:
            crossover_array3.append(breedingPair1[count])
            crossover_array4.append(breedingPair2[count])
            count+=1


    breededArray1 = crossover_array1 + crossover_array2
    breededArray2 = crossover_array2 + crossover_array4

    breedingPairs[0].string = breededArray1
    breedingPairs[1].string = breededArray2
    return breedingPairs








def main():
    print("in main")
    #initial population
    agent_array = generate_population()
    fitness(agent_array,user_string)
    breeding_pairs = selection(agent_array)
    breeding_pairs = crossover(breeding_pairs)
    print(str(breeding_pairs[0].string) + " " + str(breeding_pairs[1].string))



    #crossover

    #mutation








main()










