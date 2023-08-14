import cv2
 
#cap = cv2.VideoCapture(0)　讀鏡頭/檔案
cap = cv2.VideoCapture('opencv-fig-sample.avi')
 
while(True):
    ret, frame = cap.read()
    cv2.imshow('CTUCCE',frame)
 
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break
 
cap.release()
cv2.destroyAllWindows()
