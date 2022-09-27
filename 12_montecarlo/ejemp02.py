import numpy as np 
import random as rd


N=10**6
count=0
for i in range(N):
    point=[rd.random()*np.pi,rd.random()*2*np.pi,rd.random()]
  
    x=point[2]*np.sin(point[0])*np.cos(point[1])
    y=point[2]*np.sin(point[0])*np.sin(point[1])

    
    if ( 0.25>=((x-0.5)**2 +y**2 ) ):
        count=count+1 

vol= 4/3*np.pi
prop=float(count)/float(N)
print(prop*vol)


