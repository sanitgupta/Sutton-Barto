import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

v = np.zeros(100)
dell = np.zeros(100)
pi = np.zeros(100)

p = 0.4

while True:   
    dell[:] = v[:]    
    for i in range(0, 100):
        for b in range(1, min(i + 1, 100 - i + 1)):
            if i + b >= 100:
                R = 1
            else:
                R = v[i + b]               
            q = p * R + (1 - p) * v[max(i - b, 0)]

            if q > v[i]:
                v[i] = q
                pi[i] = b
                    
            

    if np.amax(abs(v - dell)) < 0.000000000000000000000000000000000000000001:
        print "Cv"
        break
    else:
        print "!Cv"

plt.plot(pi)
plt.show()
