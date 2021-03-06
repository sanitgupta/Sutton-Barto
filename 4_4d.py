import numpy as np
import math
import pandas as pd

def poisson_probability(mean):
    for a in range(m):
        p[a] = math.exp(-mean)
        for i in xrange(a):
            p[a] *= mean
            p[a] /= i + 1
    return p

x = np.random.poisson(5, size = None)
c1 = 0
c2 = 0
lmbd = 0.9
mc = 20
m = 10
v = np.zeros((mc + 1, mc + 1))
dell = np.zeros((mc + 1, mc + 1))
pi = np.zeros((mc + 1, mc + 1))
oldp = np.zeros((mc + 1, mc + 1))
a = 0
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
                                if pi[i, j] > 0:
                                    a = i - max(i - pi[i, j], 0)
                                else:
                                    a = max(j + pi[i, j], 0) - j
                                tempip = int(max(min(tempip - a, 20), 0))
                                tempjp = int(max(min(tempjp + a, 20), 0))
                                tempi = int(max(min(k3 + tempip - min(k1, tempip), 20), 0))
                                tempj = int(max(min(k4 + tempjp - min(k2, tempjp), 20), 0))
                                
                                r = 10 * min(k1, tempip) + 10 * min(k2, tempjp) - 2 * abs(a)
                                temp += prob1[k1, k3] * prob2[k2, k4] * (r + lmbd * v[tempi, tempj])
                v[i, j] = temp

        if np.amax(abs(v - dell)) < 5:
            print "Cv"
            break
        else:
            print "!Cv"

    oldp[:] = pi[:]
    for i in range(mc + 1):
        for j in range(mc + 1):
            q = 0
            tempv = v[i, j]
            for b in range(-5, 6):
                for k1 in range(m):
                    for k2 in range(m):
                        for k3 in range(m):
                            for k4 in range(m):
                                if b > 0:
                                    a = i - max(i - b, 0)
                                else:
                                    a = max(j + b, 0) - j
                                tempip = int(max(min(tempip - a, 20), 0))
                                tempjp = int(max(min(tempjp + a, 20), 0))
                                tempi = int(max(min(k3 + tempip - min(k1, tempip), 20), 0))
                                tempj = int(max(min(k4 + tempjp - min(k2, tempjp), 20), 0))
                                
                                r = 10 * min(k1, tempip) + 10 * min(k2, tempjp) - 2 * abs(a)
                                temp += prob1[k1, k3] * prob2[k2, k4] * (r + lmbd * v[tempi, tempj])
                                
                                q += prob1[k1, k3] * prob2[k2, k4] * (r + lmbd * v[tempi, tempj])
                if q > tempv:
                    tempv = q
                    pi[i, j] = a
    if (oldp == pi).all():
        print "Cpi"
        break
    else:
        print "!Cpi"
    


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
