#import a couple of libraries to sample random numbers
from random import random
from random import randint

stakers = []
vaults = []

#global assumptions
numStakers = 1
numVaults = 1

#the staker is an Agent - a participant in the simulated system
class Staker:
    def __init__(self, name, initBalance):
        self.name = name
        self.balance = initBalance
    def act(self):
        print("staker " + self.name + " is doing stuff")

#the other modeled entity is the Vault
class Vault:
    def __init__(self, name, initRewards):
        self.name = name
        self.balance = 0 #assume that there's nothing staked at the beginning
        self.rewards = initRewards
        #remember how much each Staker has deposited
        self.deposits = []

    def act(self):
        print("vault " + self.name + " is doing stuff")


def initStakers():
    print("initializing stakers...")
    for i in range(0, numStakers):
        name = "staker"+str(i)
        balance = randint(1, 10) #choose a random number between 1 and 10
        staker = Staker(name, balance)
        stakers.append(staker)

def initVaults():
    print("initializing vaults...")
    

def simulateStakers():
    print("simulating stakers...")

def simulateVaults():
    print("simulating vaults...")

#here will be our main simulation loop
def main():
    print("Simulation Starting...")
    #this is the number of time steps or epochs that we will run in the model
    timesteps = 1
    #initialize the entities in the model
    initStakers()
    initVaults()
    #simulation loop that iterates through all Actors in the system (e.g. Stakes and Vaults)
    for step in range(0, timesteps):
        print("simulating time step # " + str(step))
        #every time step simulate the actions of each actor
        simulateStakers()
        simulateVaults()
    print("Simulation Ending")

#python cruft - this will run the main function!
if __name__ =="__main__":
    main()