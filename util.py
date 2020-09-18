import numpy as np

def nth_power(n,power):
    return [i**power for i in range(n)]

print(nth_power(10,4))

def sigmoid(x, a=1):
    return 1/(1+np.exp(-a*x))

print(sigmoid(0.0))
