'''
Verify the LPQ conical intersections in (r_1,r_2) space
'''


Es = []
rlim = 4
r1s, r2s = np.linspace(-rlim,rlim,200),np.linspace(-rlim,rlim,200)
k1,k2 = 1,2
delta = 0
l = 1

k,g = 1,1
for r1 in r1s:
    Es_row = []
    for r2 in r2s:
#         eigenvalues = np.sort(eig(H_LVC(r1,r2,k1,k2,delta,l))[0])
        eigenvalues = np.real(np.sort(eig(H_LPQ(r1,r2,k,g))[0]))
        Es_row.append(eigenvalues)
    Es.append(Es_row)
Es = np.array(Es).transpose(2,1,0)
%matplotlib inline

diff_lim = 0.5
plt.rcParams['figure.dpi']=2000
fig,ax = plt.subplots(figsize=(9,6))
plotme = np.abs(Es[1]-Es[0])<diff_lim
pcm = ax.pcolormesh(r1s,r2s,plotme)
fig.colorbar(pcm,ax=ax)
ax.set_xlabel(r'$r_1$')
ax.set_ylabel(r'$r_2$')
ax.set_title(rf'$|E_1-E_0|<{diff_lim}$')
neaten_plot(plt.gcf())