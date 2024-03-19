from functools import reduce
# Sum of all numbers upto n raised to k.
#
# Eg: 1 + 4 + 9 + 16 + 25 would mean n = 5 and k = 2
def sigma_n_raised_to_k(n,k):
    return reduce((lambda x,y: x + y**k ), [i for i in range(n+1)])

assert sigma_n_raised_to_k(5,2) == 55