
import cv2

thresholdValue = 150
thresholdValue2 = 150
maxValue = 255

#callback method for trackbar value change
def onTrackbarValueChange(*args):
    global thresholdValue
    thresholdValue = args[0]
    print("t1 : %d" %(thresholdValue))
    #th, result = cv2.threshold(img, thresholdValue, maxValue, cv2.THRESH_TRUNC)
    th, result = cv2.threshold(img, thresholdValue, maxValue, cv2.THRESH_BINARY)
    cv2.imshow("CTUCCE", result)

def onTrackbarValueChange2(*args):
    global thresholdValue2
    thresholdValue2 = args[0]
    print("t2 : %d" %(thresholdValue2))
    #th, result = cv2.threshold(img, thresholdValue, maxValue, cv2.THRESH_TRUNC)
    th, result = cv2.threshold(img, thresholdValue2, maxValue, cv2.THRESH_BINARY_INV)
    cv2.imshow("CTUCCE", result)


#Read image 
img = cv2.imread("opencv-fig2-taken.jpg", cv2.IMREAD_GRAYSCALE)

#create window
cv2.namedWindow("CTUCCE", cv2.WINDOW_NORMAL)

#create trackbar(建立操作滑桿)
cv2.createTrackbar("THRESH_BINARY", "CTUCCE", thresholdValue, maxValue, onTrackbarValueChange)

cv2.createTrackbar("THRESH_BINARY_INV", "CTUCCE", thresholdValue, maxValue, onTrackbarValueChange2)


#call method to initialize first time
onTrackbarValueChange(thresholdValue)

while True:
    k = cv2.waitKey(10)
    
    #press esc on keyboard to exit
    if k == 27:
        break

#close all the opened windows
cv2.destroyAllWindows()