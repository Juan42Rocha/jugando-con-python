from math import sqrt
from math import cos
import  matplotlib.pyplot as plt

def rk4(f1,f2, x0, y0, v0, x1, n):
    vx = [0] * (n + 1)
    vy = [0] * (n + 1)
    vv = [0] * (n+1)
    h = (x1 - x0) / float(n)
    vx[0] = x = x0
    vy[0] = y = y0
    vv[0] = v = v0
    for i in range(1, n + 1):
        
	k1 = h * f1(x, y,v)
        l1=  h*f2(x,y,v)

	k2 = h * f1(x + 0.5 * h, y + 0.5 * k1,v +0.5*l1)
        l2 = h *f2(x+0.5*h,y+0.5*k1,v+0.5*l1)

	k3 = h * f1(x + 0.5 * h, y + 0.5 * k2,v+0.5*l2)
        l3 = h *f2(x+0.5*h,y+0.5*k2,v+0.5*l2)

        k4 = h * f1(x + h, y + k3,v+l3)  
        l4 = h*f2(x+h,y+k3,v+l3)

        vx[i] = x = x0 + i * h
        vy[i] = y = y + (k1 + k2 + k2 + k3 + k3 + k4) / 6
	vv[i] = v = v+ (l1 + l2 + l2 + l3 + l3 + l4) / 6
#print("%10.5f %10.5f %10.5f" %( x,y,v))
    return vx, vy,vv
		        
def f1(x, y,v):
    return v

def f2(x,y,v):
    k=1
    m=1
    e=0
    b=3
    return -k/m*y-e/m*v+ b*cos(2*3.1415*3*x/10)


vx, vy,vv = rk4(f1,f2, 0,0 , 1,  30, 1000)
  
for x, y,v in list(zip(vx, vy,vv))[::1]:
#   print("%10.5f %10.5f %12.4e" % (x, y, y - (4 + x * x)**2 / 16))
plt.plot(vy,vv,'.k','linewidht',0.5)
plt.show()
