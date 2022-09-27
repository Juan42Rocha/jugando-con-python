import pylab as pl
import numpy as np

pl.figure(figsize=(8,6),dpi=80)

pl.subplot(1,1,1)


x=np.linspace(-np.pi,np.pi,300,endpoint=True)

c,s=np.cos(x),np.sin(x)

pl.plot(x,c,color="blue",linewidth="1.2",linestyle="-")

pl.plot(x,s,color="blue",linewidth="1.2",linestyle="-")

pl.xlim(-4,4)

pl.xticks(np.linspace(-4,4,9,endpoint=True))

pl.ylim(-1,1)

pl.yticks(np.linspace(-1,1,5,endpoint=True))



pl.show()
