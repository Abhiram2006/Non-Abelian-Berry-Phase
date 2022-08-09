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