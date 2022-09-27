import numpy as np


def pws(a,x):
    m=len(a)

    if m!=1:
        y= a[0] + x*pws(a[1::],x)
    else:
        y= a[0]
    return y


def pws2(a,x):
    
    m = N - len(a)

    if m == 1:
        y= a[0]        
    else:
        y= a[0] + x*pws(a[1::],x)
    return y



a=[1,1,1,1]
N = len(a)
x=2
print(pws2 (a,x))

    
