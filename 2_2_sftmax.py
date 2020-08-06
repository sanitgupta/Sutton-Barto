import numpy as np
import math
import matplotlib.pyplot as plt
from random import randint

def gbf(k):
    x = 0;
    return math.exp(q[k]/T)/(np.sum(np.exp(q/T)))


def choice():
    p = np.random.random()
    s = 0
    for k in range(0, 10):
        if s < p < s + gbf(k) :
            return k;
        else :
            s = s + gbf(k)

temp = np.array([0.01, 0.1, 1,10])
for E in range(len(temp)):    
    t = 1000
    T = temp[E]
    n = 2000
    tr = np.zeros(n)
    ar = np.zeros(n)

    for i in range(0, t):
        qt = np.random.normal(0, 1, 10)
        q = np.zeros(10)
        alpha = np.ones(10)  
        for j in range(0, n):
            d = choice()
           
            r = np.random.normal(qt[d], 1, 1)
            q[d] = q[d] + (r - q[d]) * alpha[d]
            tr[j] = tr[j] + r
            alpha[d] = alpha[d]/(alpha[d] + 1)

    ar = tr/t    

    plt.plot(ar, label = T)

plt.legend(loc='upper left')
plt.show()
