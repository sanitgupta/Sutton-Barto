import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt


v = np.zeros(100)
dell = np.zeros(100)
pi = np.zeros(100)
oldp = np.zeros(100)

p = 0.4

while True:   
    while True:
        dell[:] = v[:]    
        for i in range(0, 100):
            if i + pi[i] >= 100:
                R = 1
            else:
                R = v[i + pi[i]]
            v[i] = p * R + (1 - p) * v[max(i - pi[i], 0)]                   
            v[0] = 0

        if np.amax(abs(v - dell)) < 0.0001:
            print "Cv"
            break
        else:
            print "!Cv"

    oldp[:] = pi[:]
    for i in range(0, 100):
        tempv = v[i]
        for b in range(1, i + 1):
            if i + b >= 100:
                R = 1
            else:
                R = v[i + b]               
            q = p * R + (1 - p) * v[max(i - b, 0)]
            if q > tempv:
                tempv = q
                pi[i] = b

    if (oldp == pi).all():
        print "Cpi"
        break
    else:
        print "!Cpi"


plt.plot(pi)
plt.show()
