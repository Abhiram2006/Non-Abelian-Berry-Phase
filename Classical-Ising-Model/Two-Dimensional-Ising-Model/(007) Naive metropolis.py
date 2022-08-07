'''
Imported necessary packages
'''

import numpy as np
from numpy.random import rand
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import pandas as pd

'''
Making an initial randomised 2D state
'''
def initial(N):
  initial=2*np.random.randint(2, size=(N,N))-1
  return initial

'''
Metropolis algorithm move
'''
def move(spinconfig, beta):
    for i in range(N):
        for j in range(N):
            a = np.random.randint(0, N)
            b = np.random.randint(0, N)
            s = spinconfig[a, b]
            nb = spinconfig[(a + 1)%N, b] + spinconfig[a, (b + 1)%N] + spinconfig[(a - 1)%N, b] + spinconfig[a, (b - 1)%N]
            cost = 2 * s * nb

            if cost < 0:
                s *= -1
            elif rand() < np.exp(-cost * beta):
                s *= -1
            spinconfig[a, b] = s
    return spinconfig

'''
Calculating Energy of a spin configuration
'''

def Energy(spinconfig):
    energy = 0 
    for a in range(len(spinconfig)):
        for b in range(len(spinconfig)):
            spin = spinconfig[a,b]
            neighbourspin = (spinconfig[(a+1)%size, b] + spinconfig[a,(b+1)%size] + spinconfig[(a-1)%size, b] + spinconfig[a,(b-1)%size])
            
            
            energy += -neighbour*spin
            
    return energy/2

'''
Calculating Magnetisation of a spin configuration
'''
def Magnetisation(spinconfig):
    return np.sum(spinconfig)



'''
Calculating the Energy and magnetisation with Monte-Carlo Steps
'''

size       = 10     
initialise_steps = 2**8
metropolis_steps = 2**11  

T       = np.linspace(1.25, 3.5, 60); 
E,M,C,X = np.zeros(nt), np.zeros(nt), np.zeros(nt), np.zeros(nt)
N1  = 1.0/(metropolis_steps*N**2)
N2 = 1.0/(metropolis_steps*metropolis_steps*size**2) 


for Temppoint in range(60):
    spinconfig = initial(size)         # initialise

    E0=0
    E1=0
    M0=0
    M1=0

    
    for i in range(eqSteps):       
        move(spinconfig, 1.0/T[Temppoint])          

    for i in range(mcSteps):
        move(spinconfig, 1.0/T[Temppoint])           

        E0 = E0 + Energy(spinconfig)
        M0 = M0+ Magnetisation(spinconfig)
        M1 = M1 + Magnetisation(spinconfig)*Magnetisation(spinconfig)
        E1 = E1 + Energy(spinconfig)*Energy(spinconfig)


    # divide by number of sites and iteractions to obtain intensive values    
    E[Temppoint] = E0
    M[Temppoint] = 1.0/(metropolis_steps*size**2)*M1
    C[Temppoint] = (1.0/(metropolis_steps*size**2)*E1 - 1.0/(metropolis_steps*metropolis_steps*size**2) *E0**2)*1.0/(T[Temppoint])**2
    X[Temppoint] = (1.0/(metropolis_steps*size**2)*M1 - 1.0/(metropolis_steps*metropolis_steps*size**2) *M0**2)*1.0/(T[Temppoint])
    