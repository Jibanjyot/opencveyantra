import cv2
import numpy as np

cap = cv2.VideoCapture('RoseBloom.mp4')
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc,25,(640,360))

while(cap.isOpened()):
    ret,frame= cap.read()
    if ret ==True:
        frame[:,:,0]= np.zeros([frame.shape[0],frame.shape[1]])
        frame[:, :,1] = np.zeros([frame.shape[0], frame.shape[1]])
        out.write(frame)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cap.release()
out.release()
cv2.destroyAllWindows()
