#-------------------------------------------------------------
#                       LSS: Least Sum of Square
#-------------------------------------------------------------
# To solve Least Sum of Square (LSS) using PSO.
#-------------------------------------------------------------
# Python version used: 2.7
#-------------------------------------------------------------


#-------------------------------------------------------------
# Step 1: Library Inclusion                             
#-------------------------------------------------------------
import random
import time
import numpy as np
from copy import deepcopy


startTime = time.time()

#-------------------------------------------------------------
# Step 2: Parameters
#-------------------------------------------------------------

# 2.1 PSO Parameters
algoName    = "PSOBasic"# Algo Name
c1	    = 1.5       # Acceleration constant
c2	    = 1.5       # Acceleration constant
w	    = 0.8       # Inertia weight
vLB         = -1        # Velocity Lower Bound
vUB         = 1         # Velocity Upper Bound

# 2.2 Global Parameters
iterations  = 200       # Number of iterations
popSize     = 100       # Population Size(i.e Number of Chromosomes)
pop         = []        # Store Population with Fitness
maxFunEval  = 100000    # Maximum allowable function evaluations
funEval	    = 0		# Count function evaluations
gBest       = []        # Rember Global Best chromosome
gBestFitness = []       # Rember fitness of Global Best chromosome


# 2.3 Result Saving Parameters
resultFileName="result"+algoName+".csv"


# 2.4 Stores Particle, ParticleFitness, Velocity, PBest,PBestFitness collectively;
class Individual:
    def __init__(self, P, PF, V, PB, PBF):
        self.particle=P
        self.particleFitness=PF
        self.velocity=V
        self.pBest=PB
        self.pBestFitness=PBF


# 2.5 Problem parameters
# These parameters will be re assingment later
inputFileName   = "inputData.csv"   # input data file name
D               = 0     # Problem Dimension
total           = 0     # Total no of records(rows)
LB              = 0     # Set Size Lower Bound
UB              = 0     # Set Size Upper Bound

        
#-------------------------------------------------------------
# Step 3: Fitness Functions Definitions
#-------------------------------------------------------------

# Function 1: Fitness Function
def FitnessFunction(x):
    global dataSet
    s=0
    for i in range(total):
        s = s + abs(dataSet[i][0] - dataSet[i,1:].dot(x))
    return round(s,2)
                

# Function 2: Generate Random Initial population
def Init():
    global funEval
    for i in range (0, popSize):
        particle=[]
        velocity=[]
        for j in range(0,D):
            particle.append(round(random.uniform(LB,UB),2))
            velocity.append(round(random.uniform(vLB,vUB),2))
        
        particleFitness = round(FitnessFunction(particle),2)
        funEval = funEval + 1
        newIndividual = Individual(particle, particleFitness, velocity, deepcopy(particle), particleFitness)
        pop.append(newIndividual)
        

# Function 3: Remember Global BEST in the pop;
def MemoriseGlobalBest():
    global gBest, gBestFitness
    for p in pop:
        if p.pBestFitness < gBestFitness:
            gBest = deepcopy(p.pBest)
            gBestFitness=p.pBestFitness


# Function 4: Perform PSO Operation
def PSOOperation():
    global funEval

    for i in range(0,popSize):
        for j in range(0,D):

            # Choose two random numbers
            r1=random.random()
            r2=random.random()

            # Velocity update
            pop[i].velocity[j] = w * pop[i].velocity[j] + \
                                c1 * r1 * (pop[i].pBest[j] - pop[i].particle[j]) + \
                                c2 * r2 * (gBest[j] - pop[i].particle[j])

            if pop[i].velocity[j] < vLB:
                pop[i].velocity[j] = random.uniform(vLB, vUB)
                                                    
            if pop[i].velocity[j] > vUB:
                pop[i].velocity[j] = random.uniform(vLB, vUB)

            # Particle update
            pop[i].particle[j] = round(pop[i].particle[j] + pop[i].velocity[j],2)

            if pop[i].particle[j] < LB:
                pop[i].particle[j] =  round(random.uniform(LB, UB),2)

            if pop[i].particle[j] > UB:
                pop[i].particle[j] =  round(random.uniform(LB, UB),2)


        pop[i].particleFitness = round(FitnessFunction(pop[i].particle),2)
        funEval = funEval + 1

        # Select between particle and pBest
        if pop[i].particleFitness <= pop[i].pBestFitness:
            pop[i].pBest=deepcopy(pop[i].particle)
            pop[i].pBestFitness=pop[i].particleFitness
            

    
#-------------------------------------------------------------
# Step 4: Start Program
#-------------------------------------------------------------

# Reading Data: from CSV to Matrix
dataSet=np.loadtxt(open(inputFileName,"r"),delimiter=",",skiprows=1)

# Re assinging problem parameters
D       = dataSet.shape[1] - 1  # Problem Dimension
total   = dataSet.shape[0]      # Total no of records(rows)
LB      = -10  # Set Size Lower Bound
UB      = 10   # Set Size Upper Bound


Init()
gBest=pop[0].pBest
gBestFitness=pop[0].pBestFitness
MemoriseGlobalBest()

# Saving Result
fp=open(resultFileName,"w");
fp.write("Iteration,Fitness,Chromosomes\n")

# Running till number of iterations
for i in range(0,iterations):
    PSOOperation()
    MemoriseGlobalBest()
	
    if funEval >=maxFunEval:
        break
    if i%10==0:
      print "I:",i,"\t Fitness:", gBestFitness
      fp.write(str(i) + "," + str(gBestFitness) + "," + str(gBest) + "\n")

print "I:",i+1,"\t Fitness:", gBestFitness
fp.write(str(i+1) + "," + str(gBestFitness) + "," + str(gBest) + "\n")
fp.close()

print "Done"
print "\nBestFitness:", gBestFitness
print "Best particle:", gBest
print "Total Function funEval: ",funEval
print "Result is saved in", resultFileName
print "Total Time Taken: ", round(time.time() - startTime,2), " sec\n"



