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
  <img width="508" alt="Screenshot 2022-08-07 at 1 38 44 AM" src="https://userimages.githubusercontent.com/65448559/183264840-248a92ce-8b99-40bb-890d-d90fadf9ea24.png">
<p> 
