#import a couple of libraries to sample random numbers
from random import random
from random import randint
from collections import defaultdict

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
        #start with very simple "degen" behavior
        if(self.balance >= 1 and random() < 0.5): #random() < 0.5 is a 50:50 fair coin flip
            #if the coin flip is favorable then stake some tokens
            amount = randint(1, self.balance)
            #for now let's assume there's only going to be one vault EXERCISE: choose a vault intellgently
            vaults[0].deposit(self.name, amount)
            self.balance = self.balance - amount
        #TODO: remember to log the history for plotting...

#the other modeled entity is the Vault
class Vault:
    def __init__(self, name, initRewards):
        self.name = name
        self.balance = 0 #assume that there's nothing staked at the beginning
        self.rewards = initRewards
        #remember how much each Staker has deposited
        self.deposits = defaultdict(lambda: 0)

    def act(self):
        print("vault " + self.name + " is doing stuff")

    def deposit(self, who, amount):
        self.balance = self.balance + amount
        self.deposits[who] = self.deposits[who] + amount
        print("staker " + who + " deposited " + str(amount))

def initStakers():
    print("initializing stakers...")
    for i in range(0, numStakers):
        name = "staker"+str(i)
        balance = randint(1, 10) #choose a random number between 1 and 10
        staker = Staker(name, balance)
        stakers.append(staker)

def initVaults():
    print("initializing vaults...")
    for i in range(0, numVaults):
        name = "vault"+str(i)
        rewards = randint(3,9) #choose a random number.. play with this range
        vault = Vault(name, rewards)
        vaults.append(vault)

def simulateStakers():
    print("simulating stakers...")
    #every time step make each staker act
    for staker in stakers:
        staker.act() 

def simulateVaults():
    print("simulating vaults...")
    #every time step make each vault act
    for vault in vaults:
        vault.act()

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