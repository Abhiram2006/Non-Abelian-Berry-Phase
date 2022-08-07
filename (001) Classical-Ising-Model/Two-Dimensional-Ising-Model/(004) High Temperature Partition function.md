Firstly we have to notice that βJ << 1, so we need to somehow expand the partition function with the help of this condition.

<p align="center">
<img width="539" alt="Screenshot 2022-08-07 at 1 37 12 AM" src="https://user-images.githubusercontent.com/65448559/183264647-e0b4f33e-86c8-4593-9121-55701a7f737b.png"
<p>
  
Now we can use the fact the product σiσj only takes ±1.
<p align="center">
<img width="747" alt="Screenshot 2022-08-07 at 1 37 26 AM" src="https://user-images.githubusercontent.com/65448559/183264679-cc967018-d8f5-484d-b467-5aecbeac5a5e.png"
<p>
  
Using this the partition function becomes:
  
<p align="center">
<img width="544" alt="Screenshot 2022-08-07 at 1 37 36 AM" src="https://user-images.githubusercontent.com/65448559/183264690-ea98a7c8-3baf-45eb-bccc-ef33392506aa.png"
<p>
  
  
Where q is the number of nearest neighbours and q = 4 for the 2D square lattice.
  
At high temperatures βJ << 1 =⇒ tanh βJ << 1. We can neglect all terms other than
leading order terms:
  
<p align="center">
<img width="480" alt="Screenshot 2022-08-07 at 1 37 47 AM" src="https://user-images.githubusercontent.com/65448559/183264716-35a46d45-a721-4ad3-a5d3-3d6c10773fd2.png">
<p>

Now let us correct this formula, expanding the partition function, each power of tanh βJ is
associated to a nearest neighbour pair ⟨ij⟩. We will represent this by drawing a line on the
lattice:
<p align="center">
<img width="324" alt="Screenshot 2022-08-07 at 1 44 04 AM" src="https://user-images.githubusercontent.com/65448559/183264742-86fa72fa-a416-4ee8-b7a6-6ece7c86e8cb.png">
<p>
  
But there’s a problem: each factor of tanh βJ also comes with a sum over all spins σi and σj. And these are +1 and −1 which means that they simply sum to zero:
<p align="center">
<img width="384" alt="Screenshot 2022-08-07 at 1 38 14 AM" src="https://user-images.githubusercontent.com/65448559/183264797-88d6361c-ab1f-401c-9434-37b0a8902e2f.png">
<p>
To avoid this, the only way to make sure is so that we sum over an even number of spins on
each site since then we get factors of σ^2_i^2= 1 and it does not cancel out.
<p align="center">  
  <img width="616" alt="Screenshot 2022-08-07 at 1 38 24 AM" src="https://user-images.githubusercontent.com/65448559/183264817-17aa9306-23d9-4c58-93cf-05bfa1a3e617.png">
<p> 
The partition function including the first correction becomes
<p align="center">  
  <img width="526" alt="Screenshot 2022-08-07 at 1 38 35 AM" src="https://user-images.githubusercontent.com/65448559/183264831-3edbb6ac-9a10-4053-825d-8ed292da366e.png">
<p> 
We can go further by finding the next terms by taking graphs of length 6 and the only
possibilities are:
<p align="center">  
  <img width="508" alt="Screenshot 2022-08-07 at 1 38 44 AM" src="https://user-images.githubusercontent.com/65448559/183264853-a807ea92-df2f-4755-a8dd-41fe7110c6e8.png">
<p> 
  
It gets more interesting when we look at graphs of length 8 we have four types of graphs.
Firstly there are dissconected pairs of squares:
<p align="center">  
<img width="550" alt="Screenshot 2022-08-07 at 1 38 56 AM" src="https://user-images.githubusercontent.com/65448559/183264865-bb88be75-00d5-466f-a376-f3f02c96ee30.png">
<p> 
Here the first factor N is the possible positions of the first square, and the factor N − 5 arises
because the possible location of the upper corner of the second square can’t be on any of the
vertices of the first, but nor can it be on the square one to the left of the upper corner of the
first since it would become like:
<p align="center">  
  <img width="348" alt="Screenshot 2022-08-07 at 1 39 06 AM" src="https://user-images.githubusercontent.com/65448559/183264894-59dea65e-903c-4408-9c43-fc593ce56a6c.png">
<p>
  
It has 3 lines coming off the middle site and hence it vanishes when we sum. The factor
1/2 is given to avoid over-countings. The other graphs are a large square, a rectangle and a
corner, the large square gives:
<p align="center">  
  <img width="504" alt="Screenshot 2022-08-07 at 1 39 16 AM" src="https://user-images.githubusercontent.com/65448559/183264903-c8d8a13b-c8e9-4499-9473-52bbdf9531c2.png">
<p>

 
  
There are two orientations for the rectangle so the degerancy gives factor of 2:
<p align="center">  
  <img width="512" alt="Screenshot 2022-08-07 at 1 39 29 AM" src="https://user-images.githubusercontent.com/65448559/183264915-b3774c20-fd72-4c64-8438-39d7b0957909.png">
<p>
The corner graph has four orientations giving:
<p align="center">
  <img width="630" alt="Screenshot 2022-08-07 at 1 39 53 AM" src="https://user-images.githubusercontent.com/65448559/183264943-2c1e0cce-07cf-4f93-8abe-7b5b2494b214.png">
<p>
