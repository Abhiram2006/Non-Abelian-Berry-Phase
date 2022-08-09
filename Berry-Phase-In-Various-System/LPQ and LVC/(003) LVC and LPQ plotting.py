
Es = []
r1s = np.linspace(-4,4,1000)
for r1 in r1s:
    eigenvalues = np.real(np.sort(eig(H_LVC(r1,0,1,2,1,2))[0]))
    Es.append(eigenvalues)
Es = np.array(Es)
plt.figure(figsize=(8,6))
plt.rcParams['figure.dpi']=2000
plt.plot(r1s,Es[:,0],label=r'$E_0$')
plt.plot(r1s,Es[:,1],label=r'$E_1$')
plt.xlabel(r'$r_1$')
plt.ylabel('E')
plt.title('LVC Hamiltonian')
plt.legend(fontsize=20)
neaten_plot(plt.gcf())


Es = []
r1s = np.linspace(-4,4,1000)
for r1 in r1s:
    eigenvalues = np.real(np.sort(eig(H_LPQ(r1,0.1,2,1))[0]))
    Es.append(eigenvalues)
Es = np.array(Es)
plt.rcParams['figure.dpi']=1000
plt.figure(figsize=(8,6))
plt.plot(r1s,Es[:,0],label=r'$E_0$')
plt.plot(r1s,Es[:,1],label=r'$E_1$')
plt.xlabel(r'$r_1$')
plt.ylabel('E')
plt.title('LPQ Hamiltonian')
plt.legend(fontsize=20)
neaten_plot(plt.gcf())
