import cv2

cap = cv2.VideoCapture('opencv-fig3-cars.mp4')
mog = cv2.createBackgroundSubtractorMOG2()
#mog = cv2.createBackgroundSubtractorKNN()
#mog = cv2.bgsegm.createBackgroundSubtractorMOG() # pip install opencv-contrib-python
#mog = cv2.bgsegm.createBackgroundSubtractorGMG() # pip install opencv-contrib-python


while (1):
    grabbed, frame = cap.read()
    fgmask = mog.apply(frame)
    cv2.imshow('KNN', fgmask)
    key = cv2.waitKey(200) & 0xFF

    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()