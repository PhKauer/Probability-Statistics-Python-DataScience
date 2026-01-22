# Probability-Statistics-Python-DataScience
Exercises and projects from UCSanDiegoX DSE210x course:  "Probability and Statistics in Data Science using Python"

Exercise 1:
Write a function, seq_sum(n), which generates  n  random coin flips from a fair coin and then returns the number of heads. A fair coin is defined to be a coin where  P( heads )=12

Exercise 2:
Write a function, estimate_prob(n,k1,k2,m), that uses seq_sum(n) to estimate the following probability:
P(k1<=number of heads in n flips<k2) 
The function should estimate the probability by running  m  different trials of seq_sum(n), probably using a for loop.
