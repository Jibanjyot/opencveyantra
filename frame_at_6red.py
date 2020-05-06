import cv2
import numpy as np
img = cv2.imread('frame_as_6.jpg')
img[:,:,0]= np.zeros([img.shape[0],img.shape[1]])
img[:,:,1]= np.zeros([img.shape[0],img.shape[1]])
cv2.imshow('frame',img)
cv2.imwrite('frame_at_6red.jpg',img)


