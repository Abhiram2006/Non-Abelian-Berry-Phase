'''
Here we define two Hamiltonians in matrix form, which each depend on two independent parameters  π1 and π2  and exhibit a conical intersection:

The Linear Vibronic Coupling (LVC) model is the simplest perturbation to a two-state, 2D harmonic oscillator system that exhibits a conical intersection. 
Its off-diagonal terms are linear in the coordinates, and it exhibits a single conical intersection at π1=Ξ/(π1βπ2),  π2=0.


The Linear Plus Quadratic (LPQ) model is the next most complex perturbation to the two-state, 2D harmonic oscillator system.
It exhibits four distinct conical intersections, one at  π1=π2=0  and three at  π=sqrt(r2^2+r1^2) and  π=tanβ1(π2/π1)=π/3, π, and 5π/3.
'''

def H_0(r1,r2,omega):
    return 0.5*omega**2*(r1**2+r2**2)*np.identity(2)

def H_LVC(r1,r2,k1,k2,delta,l,omega=0.2):
    return H_0(r1,r2,omega) + np.array([[k1*r1,l*r2],[l*r2,delta+k2*(r1+r2)]])
    
def H_LPQ(r1,r2,k,g,omega=1):
    rho = np.sqrt(r1**2+r2**2)
    theta = np.arctan2(r2,r1)
    return H_0(r1,r2,omega)+np.array([[0,k*rho*np.exp(-1j*theta)+0.5*g*rho**2*np.exp(2j*theta)],
                     [k*rho*np.exp(1j*theta)+0.5*g*rho**2*np.exp(-2j*theta),0]])
