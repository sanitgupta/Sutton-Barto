import numpy as np
import math
import pandas as pd

def poisson_probability(mean):
    p = np.zeros(m)
    for a in range(m):
        p[a] = math.exp(-mean)
        for i in xrange(a):
            p[a] *= mean
            p[a] /= i + 1
    return p


lmbd = 0.9
mc = 20
m = 10
v = np.zeros((mc + 1, mc + 1))
dell = np.zeros((mc + 1, mc + 1))
pi = np.zeros((mc + 1, mc + 1))
oldp = np.zeros((mc + 1, mc + 1))



tempip = 0
tempjp = 0
prob = 0
prob1 = np.zeros((m + 1, m + 1))
prob2 = np.zeros((m + 1, m + 1))

pout1 = poisson_probability(3)
pin1 = poisson_probability(3)
pout2 = poisson_probability(4)
pin2 = poisson_probability(2)

for k1 in range(m):
    for k2 in range(m):
        prob1[k1, k2] = pout1[k1] * pin1[k2]
        prob2[k1, k2] = pout2[k1] * pin2[k2]

while True:   
    while True:
        dell[:] = v[:]    
        for i in range(mc + 1):
            for j in range(mc + 1):
                temp = 0
                for k1 in range(m):
                    for k2 in range(m):
                        for k3 in range(m):
                            for k4 in range(m):
                                tempip = min(i - pi[i, j], 20)
                                tempjp = min(j + pi[i, j], 20)
                                tempi = int(max(min(k3 + tempip - min(k1, tempip), 20), 0))
                                tempj = int(max(min(k4 + tempjp - min(k2, tempjp), 20), 0))
                                
                                r = 10 * min(k1, tempip) + 10 * min(k2, tempjp) - 2 * abs(pi[i, j])
                                temp += prob1[k1, k3] * prob2[k2, k4] * (r + lmbd * v[tempi, tempj])
                v[i, j] = temp

        if np.amax(abs(v - dell)) < 1:
            print "Cv"
            break
        else:
            print "!Cv"

    oldp[:] = pi[:]
    for i in range(mc + 1):
        for j in range(mc + 1):
            tempv = v[i, j]
            for b in range(-min(5, j), min(5, i) + 1):
                q = 0
                for k1 in range(m):
                    for k2 in range(m):
                        for k3 in range(m):
                            for k4 in range(m):
                                tempip = min(i - b, 20)
                                tempjp = min(j + b, 20)
                                tempi = int(max(min(k3 + tempip - min(k1, tempip), 20), 0))
                                tempj = int(max(min(k4 + tempjp - min(k2, tempjp), 20), 0))
                                r = 10 * min(k1, tempip) + 10 * min(k2, tempjp) - 2 * abs(b)                               
                                q += prob1[k1, k3] * prob2[k2, k4] * (r + lmbd * v[tempi, tempj])
                if q > tempv:
                    tempv = q
                    pi[i, j] = b
    if (oldp == pi).all():
        print "Cpi"
        break
    else:
        print "!Cpi"

plt.imshow(pi, cmap='hot', interpolation='nearest')
plt.show()
