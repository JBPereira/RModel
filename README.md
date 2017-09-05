# RModel
This package serves the purpose of finding the optimal budget distribution across media, to maximize campaign goal.
It models consumers' behaviour over time, and combines it with a model for response to stimulus to predict how much 
return is expected for each time stamp.
To find the optimal distribution, it finds the model parameters that minimize the loss of the return up until now, and 
then uses genetic programming (GP) to find the optimal budget distribution for the next time stamp (still to be implemented).
It could also try to maximize return over the whole campaign by finding the best model and then use GP to find optimal 
distribution across campaigns as well as over time.
