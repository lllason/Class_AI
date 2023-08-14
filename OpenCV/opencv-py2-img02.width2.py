import cv2
import numpy as np

# #img = cv2.imread('opencv-fig2-teacher.png')
img = cv2.imread('opencv-fig2-teacher2.jpg')

# step 1 dilate 填充白色將黑點去除
kernel = np.ones((3,3),np.uint8) 
img2 = cv2.dilate(img, kernel, iterations = 9)
cv2.imshow('dilate1', img2)

# ## step 2 erode 侵蝕掉多出的白色
kernel = np.ones((3,3),np.uint8) 
img3 = cv2.erode(img2, kernel, iterations = 15)
cv2.imshow('erode2', img3)

ret,img4 = cv2.threshold(img3,127,255,cv2.THRESH_BINARY)
cv2.imshow('THRESH_BINARY3',img4)

kernel = np.ones((3,3),np.uint8) 
img5 = cv2.dilate(img4, kernel, iterations = 10)
cv2.imshow('dilate4', img5)



cv2.waitKey(0)
cv2.destroyAllWindows()