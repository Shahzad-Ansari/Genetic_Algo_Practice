
import random
import string

class Agent:
    def __init__(self,legnth):
        self.legnth = legnth
        self.string = "".join(random.choice(string.ascii_letters) for i in range(legnth))
        self.fitness = -1

    def __str__(self):
        return "Random string is:" + str(self.string) + "with a fitness score of " + str(self.fitness)
    def printString(self):
        print( "Random string is:" + str(self.string) + "with a fitness score of " + str(self.fitness))

