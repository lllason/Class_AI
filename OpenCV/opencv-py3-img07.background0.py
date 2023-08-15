import cv2
import numpy as np

cap = cv2.VideoCapture('opencv-fig3-cars.mp4')
#mog = cv2.createBackgroundSubtractorMOG2()
mog = cv2.createBackgroundSubtractorKNN()
#mog = cv2.bgsegm.createBackgroundSubtractorMOG() # pip install opencv-contrib-python
#mog = cv2.bgsegm.createBackgroundSubtractorGMG() # pip install opencv-contrib-python


while (1):
    grabbed, frame = cap.read()
    fgmask = mog.apply(frame)

    # 減少雜訊(白點)處理
    kernel = np.ones((3,3),np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations = 1)
    
    cv2.imshow('KNN', fgmask)
    key = cv2.waitKey(500) & 0xFF

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()