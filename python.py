import numpy as np
import matplotlib.pyplot as plt
print("hi")
# create an black image with the square at the centre

img = np.zeros((256, 256))

for i in range(256):
    img[:,i] = i
plt.imshow(img, cmap="gray", vmin=0, vmax=255)
plt.show()