import cv2

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    cv2.imshow('CTUCCE', frame)
    key = cv2.waitKey(0) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('w'):
        cv2.imwrite('ring.background2.jpg' , frame)
cap.release()
cv2.destroyAllWindows()