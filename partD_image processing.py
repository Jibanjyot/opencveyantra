import cv2
import numpy

img = cv2.imread("horse.jpg")
img =cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

I = 0.3 *img[:,:,2]+.59 * img[:,:,1]+ 0.11 * img[:,:,0]
cv2.imshow("frame",img)
cv2.waitKey(0)
print(I)
cv2.destroyAllWindows()
