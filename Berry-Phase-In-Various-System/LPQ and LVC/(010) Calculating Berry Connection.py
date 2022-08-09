def dot_eigenvectors(v1,v2,axis=0):
    return np.sum(np.conj(v1)*v2,axis=axis)

def align_vectors(v1,v2):
    print('sign:',np.sign(dot_eigenvectors(v1,v2)))
    print('dot:',dot_eigenvectors(v1,v2)/np.abs(dot_eigenvectors(v1,v2)))
    return v1,v2*dot_eigenvectors(v1,v2)/np.abs(dot_eigenvectors(v1,v2))
    
def change_basis(operator,basis):
    return np.dot(inv(basis),np.dot(operator,basis))

def Berry_connection_LPQ(r1,r2,k,g,prior_basis,dr=0.5):
    '''
    r1,r2,k,g : parameters of LPQ Hamiltonian at point of interest
    connection : matrix of Berry connection vectors for each state, where connection[:,i] is connection for eigenstate i
    '''
    if hasattr(dr, '__iter__'):
        dr1,dr2 = dr
    else:
        dr1,dr2 = dr,dr
    
    eigenvalues,eigenvectors = eigh(H_LPQ(r1,r2,k,g))
    if np.max(np.abs(dot_eigenvectors(eigenvectors,prior_basis)))<0.5:
        eigenvectors = np.flip(eigenvectors,axis=-1)
    dotted0 = dot_eigenvectors(prior_basis,eigenvectors)
    eigenvectors = (eigenvectors.T*np.sign(np.real(dotted0))).T
    
    eigenvalues1,eigenvectors1 = eigh(H_LPQ(r1+dr1,r2+dr2,k,g))
    dotted1 = dot_eigenvectors(eigenvectors,eigenvectors1)
    eigenvectors1 = (eigenvectors1.T*np.sign(np.real(dotted1))).T
    
    connection = dot_eigenvectors(eigenvectors,eigenvectors1-eigenvectors)
    print(dot_eigenvectors(eigenvectors,eigenvectors1))
    
    return 1j*connection, eigenvectors1, eigenvalues1
