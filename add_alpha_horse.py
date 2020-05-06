import cv2
import numpy as np
img = cv2.imread('horse.jpg')


b,g,r = cv2.split(img)
a = np.ones(b.shape,dtype=b.dtype)*127
img1 = cv2.merge((b,g,r,a))


cv2.imwrite('horse_alpha.png',img1)
cv2.imshow('result',cv2.imread("horse_alpha.png"))
cv2.waitKey(0)
cv2.destroyAllWindows()
