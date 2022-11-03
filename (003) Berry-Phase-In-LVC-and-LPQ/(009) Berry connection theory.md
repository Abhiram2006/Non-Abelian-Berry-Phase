<h1> Define the Berry connection in (r_1,r_2) parameter space </h1>

The Berry connection is a vector field that tells us how much the eigenvectors change with respect to a small perturbation in  𝑟1  and  𝑟2  at each point. It is defined as follows:


<p align="center">
<img width="198" alt="Screenshot 2022-08-09 at 1 23 01 PM" src="https://user-images.githubusercontent.com/65448559/183596316-d6cd4020-a0c0-4538-bf27-aba7b9ef2514.png">
<p>





We can see that this connection is a vector-valued function for each separate eigenstate  ||𝜓𝑖⟩  in our system, which tells how much a little change in our parameters induces a little change in the eigenvector. If we think about this carefully, we can see that summing up all the little changes in our eigenvector on a path through  (𝑟1,𝑟2)  space gives the total change in the eigenvector:

<p align="center">
<img width="411" alt="Screenshot 2022-08-09 at 1 23 18 PM" src="https://user-images.githubusercontent.com/65448559/183596377-bcbcf77b-c8c7-4713-b782-b9c23fc24358.png">
<p>


If our deformation of the Hamiltonian is cyclic, our path  𝐑:{(𝑟1(𝑡),𝑟2(𝑡)|𝑡 ∈ [0,1)}  will share starting and ending points. This allows us to define the Berry phase for closed cyclic paths in parameter space:
  
<p align="center">
<img width="189" alt="Screenshot 2022-08-09 at 1 23 39 PM" src="https://user-images.githubusercontent.com/65448559/183596404-ed1e3c62-3a7e-49cf-9aff-c8958a723d08.png">
<p>



It has been shown that for paths that encircle a conical intersection in parameter space, the Berry phase can be nontrivial (𝛾_𝑖 ≠ 0). Let's build the Berry connection for the LPQ Hamiltonian defined above, integrate around the central conical intersection, and see if the overlap between the initial and final states is 1 or -1.

