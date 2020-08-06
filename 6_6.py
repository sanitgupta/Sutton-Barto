import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt
from random import randint

na = 4
Q = np.zeros((10, 7, na))
pi = np.zeros((10, 7))
w = np.zeros(10)
w = np.array([0, 0, 0, 1, 1, 1, 2, 2, 1, 0])

lx = 10
ly = 7
alpha = 0.1
eps = 0.1
lmbd = 1

for i in range(8000):
    si = randint(0, lx - 1)
    sj = randint(0, ly - 1)
    if np.random.random() < eps :
        a = randint(0, na - 1)
    else :
        a = Q[si, sj].argmax()

    while not(si == 7 and sj == 3) :
        if a == 0 :
            sit = si
            sjt = max(min(sj + w[si] + 1, ly - 1), 0)
        elif a == 1 :
            sit = min(si + 1, lx - 1)
            sjt = max(min(sj + w[si], ly - 1), 0)
        elif a == 2 :
            sit = si
            sjt = min(max(sj + w[si] - 1, 0), ly - 1)
        elif a == 3 :
            sit = max(si - 1, 0)
            sjt = max(min(sj + w[si], ly - 1), 0)
        elif a == 4 :
            sit = min(si + 1, lx - 1)
            sjt = max(min(sj + w[si] + 1, ly - 1), 0)
        elif a == 5 :
            sit = min(si + 1, lx - 1)
            sjt = min(max(sj + w[si] - 1, 0), ly - 1)
        elif a == 6 :
            sit = max(si - 1, 0)
            sjt = min(max(sj + w[si] - 1, 0), ly - 1)
        elif a == 7 :
            sit = max(si - 1, 0)
            sjt = max(min(sj + w[si] + 1, ly - 1), 0)
        elif a == 8 :
            sit = si
            sjt = max(min(sj + w[si], ly - 1), 0)

        r = - 1
        if np.random.random() < eps :
            at = randint(0, na - 1)
        else :
            at = Q[sit, sjt].argmax()
            
        Q[si, sj, a] = Q[si, sj, a] + alpha * (r + lmbd * Q[sit, sjt, at] - Q[si, sj, a])
        si = sit
        sj = sjt
        a = at
       
b = np.zeros((10, 7))
V = np.zeros((7, 10))
for i in range(10):
    for j in range(7):
        b[i, j] = Q[i, j].argmax()

for j in range (6, -1, -1):
    for i in range(10):
            if b[i, j] == 0 :
                print " ^",
            elif b[i, j] == 1:
                print "->",
            elif b[i, j] == 2:
                print "\/",
            elif b[i, j] == 3:
                print "<-",   
            elif b[i, j] == 4:
                print "/^", 
            elif b[i, j] == 5:
                print "\,",
            elif b[i, j] == 6:
                print ",/",
            elif b[i, j] == 7:
                print "^<",
            elif b[i, j] == 8:
                print "  ", 
            print "  ",
    print '\n'
print '\n'
for i in range(10):
    print w[i] * 1.0, " ",

for i in range(10):
    for j in range(7):
        V[j, i] = Q[i, j, b[i, j]]

plt.imshow(V, cmap='hot', interpolation = 'nearest')
ax = plt.gca()
ax.invert_yaxis()
plt.show()
