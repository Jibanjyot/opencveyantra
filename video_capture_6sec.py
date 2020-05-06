import cv2

cap = cv2.VideoCapture('RoseBloom.mp4') #can provide 0 to capture videoo from camera
cap.set(0,6000)
success ,image=cap.read()
if success:
    cv2.imwrite('frame_as_6.jpg',image)
    cv2.imshow('frame',image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

