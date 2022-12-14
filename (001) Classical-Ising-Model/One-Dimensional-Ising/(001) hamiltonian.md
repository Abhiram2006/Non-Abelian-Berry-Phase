The Hamiltonian of the One dimensional Ising chain has two components. The internal component, interaction betweeen spins and the external component, interaction of spin with an external magnetic field. 


Internal component:



![int](https://user-images.githubusercontent.com/65448559/182865639-f954a395-1e0b-4a62-837c-afab031a7bb7.png)


{σ} represents the spin configuration of the chain, J represents the interaction strength between adjacent spins, σ_i represents the spin at lattice site i, σ_j represents the spin at lattice site j. To avoid double-counting, we sum over edges not lattices.

Also note a very important disctinction, this Ising model is discontinuous. In the sense that its in a continuous straight line and the ends are points of discontinuity. However a continuous Ising model may be made where the chain wraps around and the ends start interacting with each other.

External component:

![d12os](https://user-images.githubusercontent.com/65448559/182869125-e0ec8d47-e849-4af9-90b6-d1b303483fa0.png)

Here µ represents the magnetic moment and h_i represents the external magnetic field at site i.

Combining both these components we arrive at:

![d12os](https://user-images.githubusercontent.com/65448559/182871473-a509db58-1c0c-463e-bbfe-cc8cf213d973.png)


This non-uniorm Ising model in general, is not solvable to solve analytically. However, an Ising model with no external magnetic field is solvable.

The Hamiltonian of such an Ising model is given by just its Internal component:

![int](https://user-images.githubusercontent.com/65448559/182865639-f954a395-1e0b-4a62-837c-afab031a7bb7.png)



The configuration probability is given by the Boltzmann distribution with inverse temperature β ≥ 0:


![diagram-20220804](https://user-images.githubusercontent.com/65448559/182872071-6ea05596-f3ae-48c3-abde-c42465cbb869.png)

where β = (kBT)−1, and the normalization constant


![diagram-20220804](https://user-images.githubusercontent.com/65448559/182873897-e047df1a-db39-46c4-964f-a18f32e6d09d.png)


The configuration probability determines the probaility of the spin configuration state occuring at EQUILIBIRUM. Note that just like a Maxwellian distribution we cannot use it if the system is not in equilibrium.

If J is negative, the model is ferromagnetic
If J is positive, the model is anti-ferromagnetic.
If J=0 it is a non-interacting spin system.







