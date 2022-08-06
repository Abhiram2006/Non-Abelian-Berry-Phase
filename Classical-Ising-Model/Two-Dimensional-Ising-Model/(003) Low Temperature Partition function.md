For low temperatures the partition function can be approximated by the sum over the first few lowest energy states, now we need to list these states.
The ground state is trivial where all the spins are up/down for example:
<p align="center" width="100%">
<img width="219" alt="Screenshot 2022-08-07 at 1 18 49 AM" src="https://user-images.githubusercontent.com/65448559/183264132-57ba099c-2663-4cd0-9850-084cdd492a5d.png">
<p>

Both these ground states have an energy E = E0 = −2NJ
We can get the first excited by flipping one spin:
<p align="center" width="100%">
<img width="285" alt="Screenshot 2022-08-07 at 1 19 12 AM" src="https://user-images.githubusercontent.com/65448559/183264133-4a885467-4fdd-4ece-815d-31960e614dfb.png">
<p>

Each spin has 4 neighbours so the cost of flipping is 4 ∗ (J − (−J))) = 8J =⇒ E1 = E0 + 8J.
Of course there are N different spins that can flip hence the 1st excited state has a degeneracy
of N.
 
We can represent these excited states in a much more useful way, where we draw only the broken (denoted by red lines) which connect two spins of opposite   orientations. We represent the flipped spins by red dots and unflipped spins by blue dots. The energy of the state can be determined just by the number of red lines.
  
The first excited state can be represented by:
<p align="center" width="100%">
<img width="348" alt="Screenshot 2022-08-07 at 1 22 45 AM" src="https://user-images.githubusercontent.com/65448559/183264222-091a1891-2000-444b-87f0-28b358f23749.png">
<p>
The next state has six broken bonds:
<p align="center" width="100%"> 
<img width="356" alt="Screenshot 2022-08-07 at 1 23 02 AM" src="https://user-images.githubusercontent.com/65448559/183264232-eac83ecf-8562-4d34-8bcd-35d8d0df9dd9.png">
<p>
 
Here the factor of 2 in degeneracy comes from the two possible orientations: horizontal or vertical of the graph.
 

More interesting things happen for the next state with 8 broken bonds, the simplest configuration has two disconnected flipped spins:
 
<p align="center" width="100%"> 
<img width="685" alt="Screenshot 2022-08-07 at 1 25 43 AM" src="https://user-images.githubusercontent.com/65448559/183264300-cc03c683-3ba8-405c-96e1-7174143112b1.png">
<p>

The factor of N comes from the position of placing the first graph; the factor of N − 5 arises because the flipped spin in the second graph can sit anywhere apart from on the five vertices used in the first graph. Finally, the factor of 1/2 arises as we double-counted the graphs.
 
There are also three more graphs with the same energy E3:
<p align="center" width="100%"> 
<img width="290" alt="Screenshot 2022-08-07 at 1 26 00 AM" src="https://user-images.githubusercontent.com/65448559/183264325-13942ea6-627f-4bbb-a65e-5beccf80c87f.png">
<p>

<p align="center" width="100%"> 
<img width="343" alt="Screenshot 2022-08-07 at 1 26 19 AM" src="https://user-images.githubusercontent.com/65448559/183264331-c9d2a1be-c99c-4a76-aaee-79593f16d89d.png">
<p>
Here the factor of 2 arises from two orientations (vertical and horizontal)
<p align="center" width="100%"> 
 <img width="323" alt="Screenshot 2022-08-07 at 1 26 31 AM" src="https://user-images.githubusercontent.com/65448559/183264354-36b2bc84-8c8d-4866-88f1-cd4de031ae76.png">
<p> 
 
Here the factor of 4 comes from the four-fold symmetry of the graph.
 
Adding all these gives us the partition function as a function of exp(−βJ).
 
<p align="center" width="100%"> 
<img width="559" alt="Screenshot 2022-08-07 at 1 31 27 AM" src="https://user-images.githubusercontent.com/65448559/183264426-811609ec-ed0a-4d0a-a7c3-6ba5209b2c5c.png">
<p> 
 
If we take log of the partition function we can observe something nice:
 
<img width="585" alt="Screenshot 2022-08-07 at 1 31 49 AM" src="https://user-images.githubusercontent.com/65448559/183264446-529e152c-e372-4ac9-8a57-b501990ab667.png">

 
 
 
 
