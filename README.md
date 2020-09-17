# Fork of Dixon-Coles-Football-Predictor (credit RyanSCodes/Dixon-Coles-Football-Predictor)

Updated to automatically fetch download data and run batch predictions, runs on Python 3.8.5

Football results predictor based on Dixon-Coles method
http://www.math.ku.dk/~rolf/teaching/thesis/DixonColes.pdf

Data from http://www.football-data.co.uk/englandm.php

Based on previous results, a home advantage parameter for all teams, and attack and defense parameters
 for each team are calculated. These parameters influence a distribution of potential goals scored for each team (Poisson) over
which probabilities can be summed to figure out the probability of a home win,
draw or home loss. The previous results are also weighted exponentially by their age (old results 
are less relevant to present form).
