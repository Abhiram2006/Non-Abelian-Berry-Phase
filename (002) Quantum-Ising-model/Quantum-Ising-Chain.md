In a quantum mechanical sense however, the statistical model gets a lot more exciting when we take the Pauli picture of spin into account as it exhibits phase transitions even in one dimension, demonstrating the marked difference between the classical and quantum cases.

<img width="415" alt="Screenshot 2022-11-03 at 11 58 11 PM" src="https://user-images.githubusercontent.com/65448559/199805378-6d121c37-8b84-4e11-ac10-6440556ec273.png">

Here 𝜎𝑘 represents the observable corresponding to spin along the kth coordinate axis.
The Hamiltonian, in compact form, for such a Quantum Ising chain, with a transverse magnetic field
in x-direction would be given by:

<img width="377" alt="Screenshot 2022-11-03 at 11 58 21 PM" src="https://user-images.githubusercontent.com/65448559/199805411-5bc9eb22-ae77-41e0-b650-0bdffec87ba5.png">

There is subtlety missing in the above equation, however. We are not multiplying the matrices, using traditional matrix multiplication. Instead, we are using an operation known as the Kronecker product, that expands the space. We need both the intrinsic and extrinsic Hamiltonians to span the whole tensor product space. So, we Kronecker product the spins with the Identity matrix until it spans the whole tensor product space.

<img width="849" alt="Screenshot 2022-11-03 at 11 58 31 PM" src="https://user-images.githubusercontent.com/65448559/199805431-c9d85185-2ca1-446d-a65a-6375a032ded0.png">

On changing the external magnetic field (global parameter), we observe a phase transition in the Ising chain. That is the energy levels split, and for a high enough value of magnetic field we should observe the degeneracy get lifted.


To verify splitting of energy levels, we graphed the eigenvalues of the Hamiltonian with respect to the external transverse magnetic field.

