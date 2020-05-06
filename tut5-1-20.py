import cv2
img1 = cv2.imread('bird.jpg',cv2.IMREAD_UNCHANGED)
height1 = int(img1.shape[0])
width1= int(img1.shape[1])
channels1 = img1.shape[2]
print(height1,width1,channels1)
print (img1[213,320])

img2 = cv2.imread('cat.jpg',cv2.IMREAD_UNCHANGED)
height2 = img2.shape[0]
width2 = img2.shape[1]
channels2 = img2.shape[2]
print(height2,width2,channels2)
print (img2[195,320])

img3 = cv2.imread('flowers.jpg',cv2.IMREAD_UNCHANGED)
height3 = img3.shape[0]
width3 = img3.shape[1]
channels3 = img3.shape[2]
print(height3,width3,channels3)
print (img1[141,320])

img4 = cv2.imread('horse.jpg',cv2.IMREAD_UNCHANGED)
height4 = img4.shape[0]
width4 = img4.shape[1]
channels4 = img4.shape[2]
print(height4,width4,channels4)
print (img1[202,320])

