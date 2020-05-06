import cv2
import numpy as np
img = cv2.imread('flowers.jpg')


bgra = cv2.cvtColor(img,cv2.COLOR_BGR2BGRA)

bgra[...,2] = 0
bgra[...,1]=0

cv2.imshow('result',bgra)
cv2.imwrite('flowers_alpha.jpg',bgra)
cv2.waitKey(0)
cv2.destroyAllWindows()
