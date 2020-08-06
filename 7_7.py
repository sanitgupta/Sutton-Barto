import numpy as np
import math
import matplotlib.pyplot as plt
from random import randint

q = np.zeros((6, 2))
nEp = 20
nT = 20
na = 2
eps = 0.05
lmbd = 0.9
gamma = 0.9
alpha = 0.1
Q = np.zeros((nT, 6, na))

for t in range(nT) :
    e = np.zeros((6, na))

    for epi in range(0, nEp):
        s = randint(0, 4)
        a = randint(0, 1)
        while True:
            r = 0
            if (a == 1 and s == 4) :
                r = 1
            if(a == 1) :
                st = s + 1
            else :
                st = s

            if np.random.random() < eps :
                at = randint(0, na - 1)
            else :
                at = Q[t, st].argmax()

            delta = r + gamma * Q[t, st, at] - Q[t, s, a]

            e[s, a] = 1
            for i in range(6):
                for j in range(na):
                    Q[t, i, j] = Q[t, i, j] + alpha * delta * e[i, j]
                    e[i, j] = lmbd * gamma * e[i, j]
            
            s = st;
            a = at;
            if s == 5 :
                break
    q = q + Q[t]

for j in range(2):
    for i in range(6):
        print q[i][j]/nT, " ",
    print

for i in range(6):
    print q[i].argmax(), " ",

