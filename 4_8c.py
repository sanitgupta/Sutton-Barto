import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

v = np.zeros(101)
dell = np.zeros(101)
pi = np.zeros(101)

p = 0.4
v[0] = 0
v[100] = 1
while True:   
    dell[:] = v[:]    
    for i in range(1, 100):
        for b in range(min(i + 1, 100 - i + 1) - 1, 0, -1):              
            q = p * v[i + b] + (1 - p) * v[i - b]

            if q > v[i]:
                v[i] = q
                pi[i] = b
                    
    if np.amax(abs(v - dell)) < 0.00000001:
        print "Cv"
        break
    else:
        print "!Cv"

plt.plot(pi)
plt.show()
