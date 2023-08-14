import numpy as np
import cv2

img = cv2.imread('opencv-fig-scene01.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hist = cv2.equalizeHist(img_gray)

res = np.vstack((img_gray, img_hist)) 
cv2.imshow('CTUCCE',res)
cv2.waitKey(0)
cv2.destroyAllWindows()