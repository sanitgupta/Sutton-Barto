import numpy as np
import math
import pandas as pd

def poisson_probability(mean):
    for a in range(0,40):
        p[a] = math.exp(-mean)
        for i in xrange(a):
            p[a] *= mean
            p[a] /= i+1
    return p

x = np.random.poisson(5, size = None)
c1 = 0
c2 = 0
lmbd = 0.9
mc = 20
m = 40
v = np.zeros((mc + 1, mc + 1))
pi = np.zeros((mc + 1, mc + 1))
b = 0
delta = np.zeros(m)
p = np.zeros(m)
prob = 0
prob1 = np.zeros((m + 1, m + 1))
prob2 = np.zeros((m + 1, m + 1))


for i in range(m):
    delta[i] = i   

pout1 = poisson_probability(3)
pin1 = poisson_probability(3)
pout2 = poisson_probability(4)
pin2 = poisson_probability(2)

for k1 in range(m):
    for k2 in range(m):
        prob1[k1, k2] = pout1[k1] * pin1[k2]
        prob2[k1, k2] = pout2[k1] * pin2[k2]
        
for t in range(10):
    dell = 0
    for i in range(mc + 1):
        for j in range(mc + 1):
            temp = v[i, j]

            for k1 in range(m):
                for k2 in range(m):
                    for k3 in range(m):
                        for k4 in range(m):#if i + k1 - k2 < 0:
                        
                    
                            r = 10 * min(k1, i) + 10 * min(k2, j)
##
##                            i_next 
##                            j_next
                            tempi = max(min(k3 + i - k1, 20), 0)
                            tempj = max(min(k4 + j - k2, 20), 0)
                            v[i, j] += prob1[k1, k3] * prob2[k2, k4] * (r + lmbd * v[tempi, tempj])
    print t       

        
##for t in range(100):
##    dell = 0
##    for i in range(mc + 1):
##        for j in range(mc + 1):
##            temp = v[i, j]
##
##            for k1 in range(40):
##                for k2 in range(40):
##                    for k3 in range(40):
##                        for k4 in range(40):
##                            r = 10 * min(k1, i) + 10 * min(k2, j)
##                            prob = pout1[k1] * pout2[k2] * pin1[k3] * pin2[k4]
##                                    
##                            i_next = max(min(i + delta[k3] - delta[k1], mc), 0)
##                            j_next = max(min(j + delta[k4] - delta[k2], mc), 0)
##                            v[i, j] += prob * (r + lmbd * v[i_next, j_next])
##
##    print i        
##
