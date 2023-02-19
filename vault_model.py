
stakers = []
vaults = []

def initStakers():
    print("initializing stakers...")

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