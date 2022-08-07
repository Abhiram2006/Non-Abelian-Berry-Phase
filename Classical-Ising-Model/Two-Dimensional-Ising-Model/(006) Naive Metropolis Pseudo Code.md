Then I made a function which flips the spins if certain conditions are obeyed. Firstly I have
to analyse the interaction of Spin at lattice site n,m with its 4 neighbours
<p align="center">
<img width="643" alt="Screenshot 2022-08-08 at 12 25 45 AM" src="https://user-images.githubusercontent.com/65448559/183306791-d457dbfe-7ee4-44dd-a417-eb8a94fc3517.png">
<p>

I also defined the configuration function:
<p align="center">
<img width="155" alt="Screenshot 2022-08-08 at 12 25 55 AM" src="https://user-images.githubusercontent.com/65448559/183306764-ff5bb4f2-bee0-490a-8649-801957e90249.png">
<p>
Flip a random spin, if the change in energy (∆E) is negative then flip it. Else flip it with a
probability of exp(−∆E·β).

