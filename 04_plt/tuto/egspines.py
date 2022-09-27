import pylab as pl
import numpy as np

pl.figure(figsize=(8,5),dpi=80)
pl.subplot(111)

x=np.linspace(-np.pi,np.pi,300,endpoint=True)

s,c=np.sin(x),np.cos(x)

pl.plot(x,s,color='red',linewidth=2.5,linestyle="-",label='seno')
pl.plot(x,c,color='blue',linewidth=2.5,linestyle="-",label='coseno')

pl.legend(loc='upper left')

t=(2./3)*np.pi
pl.plot([t ,t],[0, np.cos(t)],color='blue',linewidth=2.5,linestyle='--')
pl.scatter([t, ],[np.cos(t), ],50,color='blue')
pl.annotate(r'$cosas en una nota$',
	xy=(t,np.cos(t)),xycoords='data',
	xytext=(-100,-30),textcoords='offset points',
	fontsize=15,
	arrowprops=dict(arrowstyle="->",connectionstyle="arc3,rad=.2"))


ax=pl.gca()

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.spines['bottom'].set_position(('data',0))
ax.spines['left'].set_position(('data',0))

ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')

pl.xlim(x.min()*1.1,x.max()*1.1)
pl.xticks([-np.pi,-np.pi/2,0,np.pi/2,np.pi],
	[r'$-\pi$',r'$\pi/2$', r'$0$',r'$\pi/2$',r'$\pi$'])
pl.yticks([-1,0,1], [r'$-1$', r'$0$' r'$1$'])



pl.show()
