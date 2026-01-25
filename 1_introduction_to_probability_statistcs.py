import numpy as np


#Exercise 1

def seq_sum(n):
    """ input: n, generate a sequence of n random coin flips
        output: return the number of heads 
        Hint: For simplicity, use 1,0 to represent head,tails
    """
    #
    # YOUR CODE HERE
    #
    c_f = 2*(random.rand(n)>0.5)-1
#    print(c_f)
    count=0
    for i in range(len(c_f)):
        if c_f[i]>0:
            count += 1
    return count
# checking function 

x = seq_sum(100)
print(x)
print ([seq_sum(2) for x in range(20)])
assert np.unique([seq_sum(2) for x in  range(0,200)]).tolist() == [0, 1, 2]

#
# AUTOGRADER TEST - DO NOT REMOVE
#

#Exercise 2

def estimate_prob(n,k1,k2,m):
    """Estimate the probability that n flips of a fair coin result in k1 to k2 heads
         n: the number of coin flips (length of the sequence)
         k1,k2: the trial is successful if the number of heads is
                between k1 and k2-1
         m: the number of trials (number of sequences of length n)

         output: the estimated probability
         """
    #
    # YOUR CODE HERE
    #
    count = 0
    for i in range(m):
      n_head = seq_sum(n)
      if n_head >= k1 and n_head < k2:
        count += 1
    return count/m

# this is a small sanity check
# the true check for this function is further down

x = estimate_prob(100,45,55,1000)
print(x)
print (type(x))
assert 'float' in str(type(x))
