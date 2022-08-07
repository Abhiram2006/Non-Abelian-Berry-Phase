import numpy as np
import matplotlib.pyplot as plt

size = 10
spins_initial = np.random.choice([-1, 1], (size,size))

burn = 1500
evaluation = 2500
time_steps = burn + evaluation

s_h = 1
s_v = 1
up = np.zeros((size,size))
down = np.zeros((size,size))
left = np.zeros((size,size))
right = np.zeros((size,size))


up[1:size,:] = 1 
down[0:size-1,:] = up[1:size,:]
left[:,1:size] = 1 
right[:,0:size-1] = left[:,1:size]

def nbr_udlr(s_site, s_array):
    _size = s_array.shape[0]
    i = s_site[0]
    j = s_site[1]
    
    if i == 0:
        up_site = 0
        down_site = [i+1, j]
    elif i == _size-1:
        up_site = [i-1,j]
        down_site = 0
    else:
        up_site = [i-1,j]
        down_site = [i+1, j]
    if j == 0:
        left_site = 0
        right_site = [i,j+1]
    elif j == size-1:
        left_site = [i,j-1]
        right_site = 0
    else:
        left_site = [i,j-1]
        right_site = [i,j+1]
    
    return [up_site, down_site, left_site, right_site]


def int_strength(s_site, udlr, up_array, down_array, left_array, right_array):
    if udlr == 0:
        return up_array[s_site[0], s_site[1]]
    if udlr == 1:
        return down_array[s_site[0], s_site[1]]
    if udlr == 2:
        return left_array[s_site[0], s_site[1]]
    if udlr == 3:
        return right_array[s_site[0], s_site[1]]

def energy_calc(s_array, up_array, down_array, left_array, right_array):
    _N = s_array.shape[0]
    energy = 0
    for i in range(_size):
        for j in range(_size):
            if i == 0:
                up_neighbour = 0
                down_neighbour = s_array[i+1,j]
            elif i == size-1:
                up_neighbour = s_array[i-1,j]
                down_neighbour = 0
            else:
                up_neighbour = s_array[i-1,j]
                down_neighbour = s_array[i+1,j]
            if j == 0:
                left_neighbour = 0
                right_neighbour = s_array[i,j+1]
            elif j == size-1:
                left_neighbour = s_array[i,j-1]
                right_neighbour = 0
            else:
                left_neighbour = s_array[i,j-1]
                right_neighbour = s_array[i,j+1]
        
            energy += s_array[i,j]*(up_array[i,j]*up_neighbour + down_array[i,j]*down_neighbour + left_array[i,j]*left_neighbour + right_array[i,j]*right_neighbour)
    return -energy/2
    
def wolff_step(bt, s_array, up_array, down_array, left_array, right_array):
    _N = s_array.shape[0]
    initial_site = np.random.choice(_N, 2)
    initial_site = [initial_site[0], initial_site[1]]
    old_spin = s_array[initial_site[0], initial_site[1]]
    cluster = [initial_site]
    stack = [initial_site]
    
    while stack != []:
        site = stack[np.random.choice(len(stack))]
       

        nbr = nbr_udlr(site, s_array)
        for i in range(4):
            nbr_live = nbr[i]
            if nbr_live == 0:
                continue
            nbr_spin = s_array[nbr_live[0], nbr_live[1]]
            if nbr_spin == old_spin:
                if nbr_live not in cluster:
                    p = 1 - np.exp(-2*bt*int_strength(site, i, up_array, down_array, left_array, right_array))
                    if np.random.random() < p:
                        cluster.append(nbr_live)
                        stack.append(nbr_live)
        stack.remove(site)
    
    for site in cluster:
        s_array[site[0], site[1]] *= -1
    return s_array
