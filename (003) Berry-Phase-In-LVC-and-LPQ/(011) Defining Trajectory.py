'''
Defining trajectories
Here we define 5 trajectories in  (𝑟1,𝑟2)  space which all proceed in a circular fashion counterclockwise 
around a central point. Trajectories 0-3 encircle each of the four conical intersections exhibited by the LPQ Hamiltonian 
from above, while trajectory 4 does not encircle a conical intersection.
'''


ts = np.linspace(0,1,1000)
radius = 0.7
r1_path0,r2_path0 = radius*np.cos(2*np.pi*ts), radius*np.sin(2*np.pi*ts)
r1_path1,r2_path1 = radius*np.cos(2*np.pi*ts)+1, radius*np.sin(2*np.pi*ts)+np.sqrt(3)
r1_path2,r2_path2 = radius*np.cos(2*np.pi*ts)+1, radius*np.sin(2*np.pi*ts)-np.sqrt(3)
r1_path3,r2_path3 = radius*np.cos(2*np.pi*ts)-2, radius*np.sin(2*np.pi*ts)
r1_path4,r2_path4 = radius*np.cos(2*np.pi*ts)+2, radius*np.sin(2*np.pi*ts)

diff_lim = 0.5
fig,ax = plt.subplots(figsize=(9,6))
plotme = np.abs(Es[1]-Es[0])<diff_lim
pcm = ax.pcolormesh(r1s,r2s,plotme)
fig.colorbar(pcm,ax=ax)
ax.set_xlabel(r'$r_1$')
ax.set_ylabel(r'$r_2$')
ax.set_title(rf'$|E_1-E_0|<{diff_lim}$')
ax.plot(r1_path0,r2_path0,color='g')
ax.plot(r1_path1,r2_path1,color='r')
ax.plot(r1_path2,r2_path2,color='b')
ax.plot(r1_path3,r2_path3,color='y')
ax.plot(r1_path4,r2_path4,color='y',linestyle='--')
neaten_plot(plt.gcf())