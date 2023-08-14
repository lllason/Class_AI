import numpy as np
import cv2

"""
equalizeHist (等化)
影像處理中常用的圖像增強技巧，

用數值方法將圖片的size變大，增加圖片對比度(CLAHE)
"""

img = cv2.imread('opencv-fig-scene01.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_hist = cv2.equalizeHist(img_gray)

## hstack 水平並排
res = np.hstack((img_gray, img_hist)) 
cv2.imshow('CTUCCE',res)

## vstack 垂直並排
res = np.vstack((img_gray, img_hist)) 
cv2.imshow('CTUCCE2',res)

cv2.waitKey(0)
cv2.destroyAllWindows()