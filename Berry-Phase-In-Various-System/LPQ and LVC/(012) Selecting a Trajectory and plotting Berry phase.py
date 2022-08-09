'''
Selecting a trajectory to explore
Change the trajectory variable between 0 and 4 to select a specific trajectory to follow. 
Then, for each point along the curve in this trajectory, compute the Berry connection vector
and dot it into the vector representing the next step in  (𝑟1,𝑟2)  space. 
The calculation of the connection and the dot product are both accomplished in the Berry_connection_LPQ() function. 
Keep track of all of these incremental Berry connections, as well as the cumulative Berry connection along the path.
'''

trajectory = 0

exec(f'r1_path,r2_path = r1_path{trajectory},r2_path{trajectory}')
dotted_connections = []
summed_connections = []
dr = np.diff(np.array([r1_path,r2_path]),axis=1)

_,original_basis = eigh(H_LPQ(r1_path[0],r2_path[0],k,g))
prior_basis = np.copy(original_basis)
for i,t in enumerate(ts[:-1]):
    connection,prior_basis,eigenvalues = Berry_connection_LPQ(r1_path[i],r2_path[i],k,g,prior_basis,dr=dr[:,i])
    dotted_connections.append(connection)
    summed_connections.append(np.sum(np.array(dotted_connections),axis=0))
dotted_connections = np.real(np.array(dotted_connections))
summed_connections = np.real(np.array(summed_connections))

'''
Plotting the result
Now plot the total integrated Berry connection along the path. What you should see is that for trajectories 0-3, 
the summed Berry connection is equal to  𝜋  or  −𝜋  at the end, while for trajectory 4 it returns to  0 .
This total integrated Berry connection around a closed path is equal to the Berry phase.
'''

plt.rcParams['figure.dpi'] =1000
plt.figure(figsize=(8,6))
plt.plot(ts[:-1],summed_connections[:,0],label=r'$\gamma_0$')
plt.plot(ts[:-1],summed_connections[:,0],label=r'$\gamma_1$',linestyle='--')
plt.xlabel(r'$t$')
plt.ylabel(r'$\gamma(t)$')
plt.title('Integrated Berry Phase')
plt.legend(fontsize=20)
neaten_plot(plt.gcf())