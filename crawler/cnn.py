from PIL import Image
import keras
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage import io, color
from skimage import exposure

#Load Image
x = Image.open('./inputs/a2.png')
x=np.asarray(x)

#Convolution Kernel
kernel = np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])

image = cv2.filter2D(x,-1,kernel)
plt.imshow(image, cmap=plt.cm.gray)
plt.axis('off')
plt.show()