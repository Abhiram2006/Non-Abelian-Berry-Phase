import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import eig

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

            
def H(J,h1,h2,g=0):
    array = [[-2*J+g,h2,h1,0],[h2,2*J,0,h1],[h1,0,2*J,h2],[0,h1,h2,-2*J-g]]
    return np.array(array)

I = np.array([[1,0],[0,1]])
X = np.array([[0,1],[1,0]])
Y = np.array([[0,1j],[-1j,0]])
Z = np.array([[1,0],[0,-1]])

def H_big(J,hs):
    size = len(hs)
    H_pairs = []
    H_sites = []
    for i in range(1,size):
        Ids_before = max(i-1,0)
        Ids_after = min(size-i-1,size-1)
        H_pair = np.array([1])
        for before in range(Ids_before):
            H_pair = np.kron(I,H_pair)
        H_pair = np.kron(H_pair,Z)
        H_pair = np.kron(H_pair,-J*Z)
        for after in range(Ids_after):
            H_pair = np.kron(H_pair,I)
        H_pairs.append(H_pair)
    H_pairs = np.array(H_pairs)
    H_ising = np.sum(H_pairs,axis=0)
    for i in range(size):
        Ids_before = i
        Ids_after = size-i-1
        H_site = np.array([1])
        for before in range(Ids_before):
            H_site = np.kron(I,H_site)
        H_site = np.kron(H_site,hs[i]*X)
        for after in range(Ids_after):
            H_site = np.kron(H_site,I)
        H_sites.append(H_site)
    H_sites = np.array(H_sites)
    H_field = np.sum(H_sites,axis=0)
    return H_ising+H_field
