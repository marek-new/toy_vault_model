# toy_vault_model
an educational example for the New Order founder bootcamp

## Definitions

### Staker
Each Staker $i$ is an actor having a balance $b_i$ of tokens and the Staker can stake these tokens in vaults (described below). Each Staker has its own expectation of yield $x_i$.

$I$ is the set or collection of all Stakers such that $i \in I$

### Vault
Each Vault $j$ maintains a deposit balance $s_{ij}$ for each Staker $i$.

Each Vault $j$ holds a total amount of stake $S_j$ deposited by each Staker $i$ such that $\sum s_{ij} = S_j$

Each Vault has an incoming reward stream $R_j$ that is distributed amongst Stakers each epoch or time step.

$I$ is the set or collection of all Stakers such that $i \in I$


## Relationships

### Reward distribution
Assumption: for the time being only consider _one_ reward stream.

The reward $r_{ij}$ for each Staker $i$ from Vault $j$ is 

$\forall i,\forall j: r_{ij} = \frac{s_{ij}}{S_j}* R_j$
