Let us say, we have a 2D lattice of spins in their ground state. We can flip a bunch of spins together, making a droplet of anti-aligned spins. The enthalpy cost to make such a droplet would be 2JL, it scales with the perimeter as only the spins at the edge are mis-aligned with the lattice. How many ways/degeneracies are present for such a droplet? One can travel in 4 directions from a point on a lattice, but since we dont want the path to self intersect, the number of ways to make a closed path of length L would be:

![diagram-20220807](https://user-images.githubusercontent.com/65448559/183263667-e0f0a95b-8eaa-46df-88ae-e64b3c5ce691.png)

And for there should be a ordered magnetic phase, the partition function should converge:

![diagram-20220807](https://user-images.githubusercontent.com/65448559/183263749-631a1e22-d496-4c80-a763-4ecfb38f3463.png)
The temperature above which the partition function no longer converges and disorder proceeds, is the critical temperature, which can be approximated to be:



![diagram-20220807](https://user-images.githubusercontent.com/65448559/183263816-ad71b184-17f2-40f3-8956-922df5baf00b.png)

This was how Peierls first came about proving that a phase transition in 2 dimensions is inevitable. Before we examine this behaviour, we need to understand the relation between the two extremes from the point of phase transition.
