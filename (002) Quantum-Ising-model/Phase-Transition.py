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
  
gs=[]
for i in range(-200,201):
    gs.append(i/100)

Es=[]
for g in gs:
      Es.append(np.sort(eig(H_big(1,[g, g,g,  g]))[0]))
Es=np.array(Es)

plt.plot(gs,Es)

Es = []
hlim = 5
h1s, h2s = np.linspace(-hlim,hlim,100),np.linspace(-hlim,hlim,100)
g = -0.5
for h1 in h1s:
    Es_row = []
    for h2 in h2s:
        eigenvalues = np.sort(eig(H(1,h1,h2,g=g))[0])
        Es_row.append(eigenvalues)
    Es.append(Es_row)
Es = np.array(Es).transpose(2,1,0)
Es.shape


%matplotlib inline
fig,ax = plt.subplots(2,2,figsize=(17,15))
counter = 0
for i in range(2):
    for j in range(2):
#         exec(f'pcm{counter} = ax[{i},{j}].pcolormesh(h1s,h2s,Es[{counter}])')
#         exec(f'fig.colorbar(pcm{counter},ax=ax[{i},{j}])')
        pcm = ax[i,j].pcolormesh(h1s,h2s,Es[counter])
        fig.colorbar(pcm,ax=ax[i,j])
        ax[i,j].set_xlabel(r'$h_1$')
        ax[i,j].set_ylabel(r'$h_2$')
        ax[i,j].set_title(f'E{counter}')
        counter+=1
neaten_plot(plt.gcf())


%matplotlib notebook
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

fig = plt.figure()
ax = Axes3D(fig)
H1s,H2s = np.meshgrid(h1s,h2s)

# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surf0 = ax.plot_surface(H1s,H2s, Es[0],vmin=-7,vmax=7,cmap=cm.coolwarm,linewidth=1, antialiased=False)
surf1 = ax.plot_surface(H1s,H2s, Es[1],vmin=-7,vmax=7,cmap=cm.coolwarm,linewidth=1, antialiased=False)
surf2 = ax.plot_surface(H1s,H2s, Es[2],vmin=-7,vmax=7,cmap=cm.coolwarm,linewidth=1, antialiased=False)
surf3 = ax.plot_surface(H1s,H2s, Es[3],vmin=-7,vmax=7,cmap=cm.coolwarm,linewidth=1, antialiased=False)
ax.set_zlim(-7,7)
ax.set_xlabel(r'$h_1$')
ax.set_ylabel(r'$h_2$')



J = 1
h_max = 5
h3 = 1.5
phis = np.linspace(0,2*np.pi,100)
rs = np.linspace(0,h_max,20)

Es = []
for rr,r in enumerate(rs):
    Es_row = []
    for phi in phis:
        h1 = np.round(r*np.cos(phi),2)
        h2 = np.round(r*np.sin(phi),2)        
        eigenvalues = np.real(np.sort(eig(H_big(J,[h3,h1,h2]))[0]))
#         if rr==len(rs)-1:
#             print(h1,h2)
        Es_row.append(eigenvalues)
    Es.append(Es_row)
Es = np.array(Es).transpose(2,1,0)
Es.shape
