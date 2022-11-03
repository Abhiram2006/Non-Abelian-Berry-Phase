import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from numpy.linalg import eig,norm,inv,det,svd
from scipy.linalg import eigh
import qutip as qt

param_dict = {'spinewidth':2,
              'linewidth':4,
              'ticklength':6,
              'tickwidth':3,
              'ticklabelsize':15,
              'axislabelsize':20,
              'titlesize':23}
import matplotlib
def neaten_plot(neatenme, param_dict=param_dict):
    if isinstance(neatenme,matplotlib.figure.Figure):
        for ax in neatenme.axes:
            neaten_plot(ax)
        plt.tight_layout()
    elif isinstance(neatenme,matplotlib.axes.Axes):
        neatenme.tick_params(labelsize=param_dict['ticklabelsize'],length=param_dict['ticklength'],width=param_dict['tickwidth'])
        neatenme.xaxis.get_label().set_fontsize(param_dict['axislabelsize'])
        neatenme.yaxis.get_label().set_fontsize(param_dict['axislabelsize'])
        try:
            neatenme.zaxis.get_label().set_fontsize(param_dict['axislabelsize'])
        except Exception:
            pass
        neatenme.title.set_fontsize(param_dict['titlesize'])
        for axis in ['top','bottom','left','right']:
            neatenme.spines[axis].set_linewidth(param_dict['spinewidth'])
        for line in neatenme.lines:
            line.set_linewidth(param_dict['linewidth'])   
            
            
import scipy.linalg as la
from qutip.qobj import Qobj

def orthogonalize(vecs,tol=1e-3):
    for j in range(1, vecs.shape[1]):
        for k in range(j):
            dot = vecs[:, j].dot(vecs[:, k].conj())
            if np.abs(dot) > tol:
                vecs[:, j] = ((vecs[:, j] - dot * vecs[:, k])
                              / (1 - np.abs(dot)**2)**0.5)
    return vecs

def _degen(tol, vecs, ops, i=0):
    """
    Private function that finds eigen vals and vecs for degenerate matrices..
    """
    if len(ops) == i:
        return vecs

    # New eigenvectors are sometime not orthogonal.
    for j in range(1, vecs.shape[1]):
        for k in range(j):
            dot = vecs[:, j].dot(vecs[:, k].conj())
            if np.abs(dot) > tol:
                vecs[:, j] = ((vecs[:, j] - dot * vecs[:, k])
                              / (1 - np.abs(dot)**2)**0.5)

    subspace = vecs.conj().T @ ops[i].data @ vecs
    eigvals, eigvecs = la.eig(subspace)

    perm = np.argsort(eigvals)
    eigvals = eigvals[perm]

    vecs_new = vecs @ eigvecs[:, perm]
    for k in range(len(eigvals)):
        vecs_new[:, k] = vecs_new[:, k] / la.norm(vecs_new[:, k])
        # new Ian stuff, normalize largest component to be real
        maxval = vecs_new[np.argmax(np.abs(vecs_new[:, k])),k]
        vecs_new[:, k] = vecs_new[:, k] / maxval*np.abs(maxval)

    k = 0
    while k < len(eigvals):
        ttol = max(tol, tol * abs(eigvals[k]))
        inds, = np.where(abs(eigvals - eigvals[k]) < ttol)
        if len(inds) > 1:  # if at least 2 eigvals are degenerate
            vecs_new[:, inds] = _degen(tol, vecs_new[:, inds], ops, i+1)
        k = inds[-1] + 1
    return vecs_new


def my_simdiag(ops, evals: bool = True, *,
            tol: float = 1e-14, safe_mode: bool = True):
    """Simultaneous diagonalization of commuting Hermitian matrices.

    Parameters
    ----------
    ops : list/array
        ``list`` or ``array`` of qobjs representing commuting Hermitian
        operators.

    evals : bool [True]
        Whether to return the eigenvalues for each ops and eigenvectors or just
        the eigenvectors.

    tol : float [1e-14]
        Tolerance for detecting degenerate eigenstates.

    safe_mode : bool [True]
        Whether to check that all ops are Hermitian and commuting. If set to
        ``False`` and operators are not commuting, the eigenvectors returned
        will often be eigenvectors of only the first operator.

    Returns
    --------
    eigs : tuple
        Tuple of arrays representing eigvecs and eigvals of quantum objects
        corresponding to simultaneous eigenvectors and eigenvalues for each
        operator.

    """
    if not ops:
        raise ValueError("No input matrices.")
    N = ops[0].shape[0]
    num_ops = len(ops) if safe_mode else 0
    for jj in range(num_ops):
        A = ops[jj]
        shape = A.shape
        if shape[0] != shape[1]:
            raise TypeError('Matricies must be square.')
        if shape[0] != N:
            raise TypeError('All matrices. must be the same shape')
        if not A.isherm:
            raise TypeError('Matricies must be Hermitian')
        for kk in range(jj):
            B = ops[kk]
            if (A * B - B * A).norm() / (A * B).norm() > tol:
                raise TypeError('Matricies must commute.')

    eigvals, eigvecs = la.eig(ops[0].full())
    perm = np.argsort(eigvals)
    eigvecs = eigvecs[:, perm]
    eigvals = eigvals[perm]

    k = 0
    while k < N:
        # find degenerate eigenvalues, get indicies of degenerate eigvals
        ttol = max(tol, tol * abs(eigvals[k]))
        inds, = np.where(abs(eigvals - eigvals[k]) < ttol)
        if len(inds) > 1:  # if at least 2 eigvals are degenerate
            eigvecs[:, inds] = _degen(tol, eigvecs[:, inds], ops, 1)
        k = inds[-1] + 1

    for k in range(N):
        eigvecs[:, k] = eigvecs[:, k] / la.norm(eigvecs[:, k])

    kets_out = [
        Qobj(eigvecs[:, j],
             dims=[ops[0].dims[0], [1]], shape=[ops[0].shape[0], 1])
        for j in range(N)
    ]
    eigvals_out = np.zeros((len(ops), N), dtype=np.float64)
    if not evals:
        return kets_out
    else:
        for kk in range(len(ops)):
            for j in range(N):
                eigvals_out[kk, j] = ops[kk].matrix_element(kets_out[j],
                                                            kets_out[j]).real
        return eigvals_out, kets_out



I= np.array([[1,0], [0,1]])
Sz=np.array([[1,0], [0,-1]])
Sx=np.array([[0,1], [1, 0]])
Sy=np.array([[0,-1j], [1j, 0]])

def H(J, gx, gy, gz,N=1):
    H_elements = []
    for i in range(N):
        H_spin = 1
        for j in range(i):
            H_spin = np.kron(H_spin,I)
        H_spin = np.kron(H_spin,-1*(gx*Sx + gy*Sy + gz*Sz))
        for j in range(N-i-1):
            H_spin = np.kron(H_spin,I)
        H_elements.append(H_spin)
    H_field=np.sum(np.array(H_elements),axis=0)
    Hps=[]  
    for i in range(N-1):
        Hp=1
        for b in range(i):
            Hp=np.kron(I,Hp)
        Hp=np.kron(np.kron(Hp, gx*Sx + gy*Sy + gz*Sz), -J*(gx*Sx + gy*Sy + gz*Sz))
        for a in range(N-i-2):
            Hp=np.kron(Hp, I)
        Hps.append(Hp)
            
    H_int=np.sum(np.array(Hps), axis=0)
    return H_field+H_int
  
def dot_eigenvectors(v1,v2,axis=0):
    return np.sum(v1.conj()*v2,axis=axis)

def change_basis(operator,basis):
    return np.matmul(inv(basis),np.matmul(operator,basis))

def fnsigma_b(gx,gy,gz, N):
    sigma_elements=[]
    
    for i in range(N):
        H_spin = 1
        for j in range(i):
            H_spin = np.kron(H_spin,I)
        H_spin = np.kron(H_spin,(gx*qt.jmat(0.5,'x') + gy*qt.jmat(0.5,'y') + gz*qt.jmat(0.5,'z')))
        for j in range(N-i-1):
            H_spin = np.kron(H_spin,I)
        sigma_elements.append(H_spin)
    sigma_field=np.sum(np.array(sigma_elements),axis=0)
    sigma_field=sigma_field/(np.sqrt(gx**2+gy**2+gz**2))
    return sigma_field

def J1(gx,gy,gz,N=2):
    op = fnsigma_b(gx,gy,gz,N=1)
    for i in range(N-1):
        op = np.kron(op,np.identity(2))
    return op

def J2(gx,gy,gz,N=2):
    op = H(0.5,gx,gy,gz,N=N)
    e,basis = eigh(op)
    basis = orthogonalize(basis)
    for i in range(4):
        maxval = basis[np.argmax(np.abs(basis[:,i])),i]
        basis[:,i] = basis[:,i]*np.abs(maxval)/maxval
    e = np.round(e,3)
    matrix = np.zeros((4,4))
    for ue in np.unique(e):
        indices = np.argwhere(ue==e)[:,0]
        if indices.size>1:
            matrix[indices[0],indices[1]] = 1
            matrix[indices[1],indices[0]] = 1
            matrix[indices[0],indices[0]] = 1
            matrix[indices[1],indices[1]] = 1
        else:
            matrix[indices[0],indices[0]] = 2
    
    return change_basis(matrix,inv(basis))
    
    


def Berry_connection_Ising(r1,r2,r3,prior_basis=None,dr=0.5,N=2):

    if hasattr(dr, '__iter__'):
        dr1,dr2,dr3 = dr
    else:
        dr1,dr2,dr3 = dr,dr,dr
        
    sigma_b0 = qt.Qobj(fnsigma_b(r1, r2, r3, N=N))
    sigma_b0 = qt.Qobj(J2(r1,r2,r3))
#     print(sigma_b0)
    H0 = qt.Qobj(H(1, r1, r2, r3,N=N))
    c = qt.commutator(H0,sigma_b0)
    if np.max(np.abs(c.full()))>0:
        print(c)
    eigenvalues0,eigenvectors0 = my_simdiag([H0,sigma_b0],evals=True,safe_mode=True,tol=1e-3)
    ev0 = []
    for ev in eigenvectors0:
        ev0.append(ev.full())
    ev0 = np.array(ev0)[:,:,0].T

    
    sigma_b1 = qt.Qobj(fnsigma_b(r1+dr1, r2+dr2, r3+dr3, N=N))
    sigma_b1 = qt.Qobj(J2(r1+dr1,r2+dr2,r3+dr3))
    H1 = qt.Qobj(H(1, r1+dr1, r2+dr2, r3+dr3,N=N))
#     print(H1)
    c = qt.commutator(H1,sigma_b1)
    if np.max(np.abs(c.full()))>0:
        print(c)
        print('does not commute')
    eigenvalues1,eigenvectors1 = my_simdiag([H1,sigma_b1],evals=True,safe_mode=True,tol=1e-3)
    ev1 = []
    
    for ev in eigenvectors1:
        ev1.append(ev.full())
    ev1 = np.array(ev1)[:,:,0].T

    dotted = dot_eigenvectors(ev1,ev0)

    if np.abs(dotted)[1]<0.5:
        ev1[:,[1,2]] = ev1[:,[2,1]]
    dotted = dot_eigenvectors(ev1,ev0)

    
    for i in range(2,4):
        if np.sign(dot_eigenvectors(np.imag(ev0),np.real(ev1))[i])!=np.sign(dot_eigenvectors(np.imag(ev0),np.real(ev0))[i]):
            ev1[:,i]*=-1
            
            
            
    connection = dot_eigenvectors(ev0,ev1-ev0)

    return 1j*connection, ev1, eigenvalues1
  
  

%matplotlib inline
ts = np.linspace(0,1,1000)
radius = 10
r1_path0,r2_path0 = radius*np.cos(2*np.pi*ts), radius*np.sin(2*np.pi*ts)
r1_path1,r2_path1 = radius*np.cos(2*np.pi*ts), radius*np.sin(2*np.pi*ts)+3
r1_path3,r2_path3 = 4*radius*np.cos(2*np.pi*ts), 4*radius*np.sin(2*np.pi*ts)



trajectory = 0

exec(f'r1_path,r2_path = r1_path{trajectory},r2_path{trajectory}')
dotted_connections = []
summed_connections = []
Bz = 0.1
dr = np.diff(np.array([r1_path,r2_path,np.zeros_like(r1_path)]),axis=1)

N=2
eigenvalues,eigenvectors = eig(H(0.5, r1_path[0], r2_path[0],Bz,N=N))
# print(eigenvalues)
prior_basis = orthogonalize(np.copy(eigenvectors))
E_diff = [np.abs(eigenvalues[1]-eigenvalues[0])]
current_basis = [eigenvectors]
for i,t in enumerate(ts[:-1]):
    connection,prior_basis,eigenvalues = Berry_connection_Ising(r1_path[i],r2_path[i],Bz,prior_basis,dr=dr[:,i],N=N)
    dotted_connections.append(connection)
    summed_connections.append(np.sum(np.array(dotted_connections),axis=0))
    E_diff.append(np.abs(eigenvalues[1]-eigenvalues[0]))
    current_basis.append(prior_basis)
dotted_connections = np.array(dotted_connections)
summed_connections = np.array(summed_connections)
