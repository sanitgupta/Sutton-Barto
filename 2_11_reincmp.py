import numpy as np
import math
import matplotlib.pyplot as plt
from random import randint

def gbf(k):
    return math.exp(p[k])/(np.sum(np.exp(p)))


def choice():
    p = np.random.random()
    s = 0
    for k in range(0, 10):
        if s < p < s + gbf(k) :
            return k;
        else :
            s = s + gbf(k)

RR = np.array([10, 0, -10])
for E in range(len(RR)):    
    t = 1000
    n = 2000
    tr = np.zeros(n)
    ar = np.zeros(n)
    
    
    for i in range(0, t):
        qt = np.random.normal(0, 1, 10)
        p = np.zeros(10)
        alpha = 0.1
        beta = 0.1
        rr = RR[E]
        
        for j in range(0, n):
            d = choice()
           
            r = np.random.normal(qt[d], 1, 1)
            p[d] = p[d] + beta * (r - rr)
            rr = rr + alpha * (r - rr)
            tr[j] = tr[j] + r
           
    ar = tr/t    

    plt.plot(ar, label = RR[E])

plt.legend(loc='upper left')

plt.show()
