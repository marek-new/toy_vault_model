'''
excercises (try them in any order you like, some are easier than others):
#1 change the number of stakers (easy)
#2 increase number of timesteps (easy)
#3 introduce a second token type to incentivise users to stay in the vault longer (tough)
#4 add more than one vault (tough)
#5 introduce a randomized yield instead of constant
#6 more sophisticated staking behavior than "random degen"
#7 update the mathematical specification based on your updates to the python model
'''

#import a couple of libraries to sample random numbers
from random import random
from random import randint
from collections import defaultdict
import numpy as np
import matplotlib.pyplot as plt

stakers = []
vaults = []

#global assumptions
numStakers = 4
numVaults = 1

 #this is the number of time steps or epochs that we will run in the model
timesteps = 10

#the staker is an Agent - a participant in the simulated system
class Staker:
    def __init__(self, name, initBalance, expectedReward):
        self.name = name
        self.balance = initBalance
        self.expectedReward = expectedReward
        self.history = np.array([initBalance])
    def act(self):
        print("staker " + self.name + " is doing stuff")
        #start with very simple "degen" behavior
        if(self.balance >= 1 and random() < 0.5): #random() < 0.5 is a 50:50 fair coin flip
            #if the coin flip is favorable then stake some tokens
            print("WHAT THE FATARITY " + str(self.balance))
            amount = randint(1, int(self.balance))
            #for now let's assume there's only going to be one vault EXERCISE: choose a vault intellgently
            vaults[0].deposit(self.name, amount)
            self.balance = self.balance - amount
        elif(vaults[0].rewardShare(self.name) < self.expectedReward) and vaults[0].deposits[self.name] > 0:
            #user can claim rewards if it's more than the amount they "care about" - expectedReward
            self.balance = self.balance + vaults[0].withdraw(self.name)
        elif(random() < 0.5 and vaults[0].rewards[self.name] > 0 and self.expectedReward < vaults[0].rewards[self.name] ):
			#user not getting enough rewards (based on expectedRewards) - so withdraw from the vault
            self.balance = self.balance + vaults[0].claim(self.name)
		#else - do nothing

        self.history = np.concatenate([self.history, np.array([self.balance])] )

    def claimRewards(self):
        rewards = vaults[0].claim(self.name)
        self.balance = self.balance + rewards

#the other modeled entity is the Vault
class Vault:
    def __init__(self, name, initRewards):
        self.name = name
        self.balance = 0 #assume that there's nothing staked at the beginning
        self.rewardRate = initRewards
        #remember how much each Staker has deposited
        self.deposits = defaultdict(lambda: 0)
        #remember how many rewards are accrued to each Staker
        self.rewards = defaultdict(lambda: 0)
        #keep a history for plotting
        self.history = np.array([self.balance])
   
    def act(self):
        print("vault " + self.name + " current deposits " + str(self.balance))
        self.history = np.concatenate([self.history, np.array([self.balance])] )
        for depositor in self.deposits:
            #yield comes in and is allocated
            self.rewards[depositor] = self.rewards[depositor] + self.rewardShare(depositor)
    def deposit(self, who, amount):
        self.balance = self.balance + amount
        self.deposits[who] = self.deposits[who] + amount
        print("staker " + who + " deposited " + str(amount))

    def withdraw(self, who):
        amount = self.deposits[who]
        self.balance = self.balance - amount
        self.deposits[who] = 0
        print("staker " + who + " withdrew " + str(amount))
        return amount

    def rewardShare(self, who):
        if(self.balance == 0):
            return 0
        return self.rewardRate * self.deposits[who] / (1.0*self.balance)

    def claim(self, who):
        amount = self.rewards[who]
        self.rewards[who] = 0
        print("staker " + who + " claimed " + str(amount))

        return amount

def initStakers():
    print("initializing stakers...")
    for i in range(0, numStakers):
        name = "staker"+str(i)
        balance = randint(1, 10) #choose a random number between 1 and 10
        expectedReward = randint(1,10)
        staker = Staker(name, balance, expectedReward)
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
    #initialize the entities in the model
    initStakers()
    initVaults()
    #simulation loop that iterates through all Actors in the system (e.g. Stakes and Vaults)
    for step in range(0, timesteps):
        print("simulating time step # " + str(step))
        #every time step simulate the actions of each actor
        simulateStakers()
        simulateVaults()
    print("Simulation Ending...")
    print("Generating plots...")
    #plot vault
    plt.title("Vault Balance")
    plt.xlabel("time")
    plt.ylabel("vault balance")
    x_vals= np.linspace(0,timesteps,timesteps+1)
    plt.plot(x_vals,vaults[0].history)
    plt.show()

    #plot stakers
    plt.title("Staker Balances")
    plt.xlabel("time")
    plt.ylabel("staker balance")
    for i in range (0, numStakers):
        plt.plot(x_vals,stakers[i].history, label=stakers[i].name)
    plt.legend()
    plt.show()
    print("done.")

#python cruft - this will run the main function!
if __name__ =="__main__":
    main()