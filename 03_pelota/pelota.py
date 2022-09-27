import numpy as np
import matplotlib.pyplot as plt


n=3
x0=0.9
y0=0.2
thet=0
v=2.0

dt=0.01

arch=open("datos.dat","w")

for i in range(n):
    vx=v*np.cos(thet)
    vy=v*np.sin(thet)
    
    x=vx*dt+x0
    y=vy*dt+y0
    
   # arch.write(str(x)+str(y)+str(vx)+str(vy))
    arch.write(str(x))
   
    if (x>1):
      thet=np.pi -thet
    elif (y<0):
      thet=-thet
    elif (x<y):
      thet=np.pi*0.5-thet
      
    plt.plot(x,y,'k')
    plt.show()
    plt.install_repl_displayhook()
    
    

    x0=x
    y0=y
arch.close
