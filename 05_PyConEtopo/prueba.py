import numpy as np
import matplotlib.pyplot as plt
from skimage import io
#import skimage as sk

ima=io.imread("gorro.png")/255.0 
plt.figure()
plt.imshow(ima)
plt.show()
plt.figure()
imal= np.arange(16).reshape(4,4)
plt.imshow(imal)
plt.plot(imal)
print(ima.shape)
print("fin")
