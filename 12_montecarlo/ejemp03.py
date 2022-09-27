import numpy as np
import random as rd


N=10**6

count=0
for i in range(N):
    point=[rd.random(),rd.random(),rd.random(),rd.random()]

    d=point @np.transpose(point)
    if d<=1:
       count+=1



print(np.pi/2)
print(float(count)/float(N)/np.pi*2**len(point))
