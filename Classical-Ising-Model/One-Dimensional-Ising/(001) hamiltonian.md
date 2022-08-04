The Hamiltonian of the Ising model has two components. The internal component, interaction betweeen spins and the external component, interaction of spin with an external magnetic field. 


Internal component:



![int](https://user-images.githubusercontent.com/65448559/182865639-f954a395-1e0b-4a62-837c-afab031a7bb7.png)


{σ} represents the spin configuration, J represents the interaction strength, σ_i represents the spin at lattice site i, σ_j represents the spin at lattice site j. To avoid double-counting, we sum over edges not lattices.

Also note a very important disctinction, this ising model is discontinuous. In the sense that its in a continuous straight line and the enda are point of discontinuity. However a continuous Ising model may be made where the chain wraps around and the ends start interacting with each other.

External component:

![d12os](https://user-images.githubusercontent.com/65448559/182869125-e0ec8d47-e849-4af9-90b6-d1b303483fa0.png)

Here mu represents the magnetic moment and h_i represents the external magnetic field at site i.

Combining both these components we arrive at:

![d12os](https://user-images.githubusercontent.com/65448559/182871473-a509db58-1c0c-463e-bbfe-cc8cf213d973.png)


This non-uniorm Ising model in general, is not solvable to solve analytically. However, an Ising model with no external magnetic field is solvable.

The Hamiltonian of such an Ising model is given by just its Internal component:

![int](https://user-images.githubusercontent.com/65448559/182865639-f954a395-1e0b-4a62-837c-afab031a7bb7.png)



The configuration probability is given by the Boltzmann distribution with inverse temperature β ≥ 0:


![diagram-20220804](https://user-images.githubusercontent.com/65448559/182872071-6ea05596-f3ae-48c3-abde-c42465cbb869.png)

where β = (kBT)−1, and the normalization constant



