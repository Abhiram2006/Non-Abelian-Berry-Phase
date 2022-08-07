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
