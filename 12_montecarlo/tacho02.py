import random as random
import numpy as np
from numba import jit


N=10**5
count=0

for i in range(0,N):
    point=(random.random()*np.pi, random.random()*2*np.pi, random.random())
    x=np.cos(point[1])*np.sin(point[0])*point[2]-0.5
    y=np.sin(point[1])*np.sin(point[0])*point[2]

    if 0.25>x**2+y**2:
        count=count+1
Vol=4/3*np.pi
answer=float(count)/float(N)
print(answer*Vol)
