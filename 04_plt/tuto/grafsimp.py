import numpy as np
import pylab as pl

x=np.linspace(-np.pi,np.pi,256,endpoint=True)

c,s= np.cos(x),np.sin(x)


pl.plot(x,c)
pl.plot(x,s)

pl.show()
