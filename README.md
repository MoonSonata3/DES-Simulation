# DES-Simulation
this following repository has scripts to explore different queuing methods set.<br>

### License:
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
### Required Packages:
simpy<br>
numpy<br>
matplotlib<br>


### contents:
-MDn.py<br>
code function to get the mean waiting times using the M/D/n queing method or the deterministic service time queing

-MHn.py<br>
just the plotting for the M/H/n queing method the fuction from MDn.py was used since it pretty much handles all the heavy lifting

-q3 sjf with mm1 comparaison plot.py<br>
Here we plot the sjf model and compare it to the MM1, both ploted in fct of rho

-question three SJF with confidence intervals.py<br>
to get confidence interval for the sjf model

-Question two : FIFO for different number of servers.py<br>
  We plot M/M/n for n=1,2,4 with xaxis=rho which varies between 0.1 to 1
  
