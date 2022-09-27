import numpy as np
import matplotlib.pyplot as plt

x=np.arange(0,2,0.01)

plt.plot(x,x,label='linear')
plt.plot(x,x**2,label='quadratic')
plt.plot(x,x**3,label='cubic')

plt.xlabel("x label")
plt.ylabel("y label")

plt.legend()
plt.show()
