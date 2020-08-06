import numpy as np
import matplotlib.pyplot as plt
from random import randint

def choice():
    p = np.random.random()
    
    if p < e :
        return randint(0, 9)
    else:
        return np.argmax(q)

err = np.array([0])

for E in range(len(err)):    
    t = 1000
    n = 2000
    tr = np.zeros(n)
    ar = np.zeros(n)
    e = err[E]

    for i in range(0, t):
        qt = np.random.normal(0, 1, 10)
        q = np.ones(10) * 5
        alpha = np.ones(10) * 0.1  
        
        for j in range(0, n):
                d = choice()
               
                r = np.random.normal(qt[d], 1, 1)
                q[d] = q[d] + (r - q[d]) * alpha[d]
                tr[j] = tr[j] + r
                #alpha[d] = alpha[d]/(alpha[d] + 1)

    ar = tr/t    

    plt.plot(ar, label = e)

plt.legend(loc='upper left')
for i in range(25) :
    print i, " ", ar[i]

plt.show()
