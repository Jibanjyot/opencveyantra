import cv2
import numpy as np

img = cv2.imread('cat.jpg',cv2.IMREAD_UNCHANGED)
print(img.shape)

img[:,:,0]= np.zeros([img.shape[0],img.shape[1]])
img[:,:,1]= np.zeros([img.shape[0],img.shape[1]])

cv2.imwrite('cat_red.jpg',img)
