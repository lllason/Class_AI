import cv2
import numpy as np

img = cv2.imread('opencv-fig2-teacher.png')

## no.ones((3,3)) 3x3矩陣
"""
Erosion 影像侵蝕
用途1：Erosion 影像侵蝕對於移除影像中的小白雜點很有幫助，可用來去噪，例如影像中的小雜點，雜訊。
用途2：細化影像，消除毛刺

Dilation 影像膨脹
用途1：Dilation 影像膨脹通常是配合著影像侵蝕 Erosion 使用，先使用侵蝕的方式使影像中的線條變窄，同時也去除雜訊，之後再透過 Dilation 將影像膨脹回來。
用途2：用來連接兩個很靠近但分開的物體
"""
kernel = np.ones((3,3),np.uint8) 
erosion = cv2.erode(img, kernel, iterations = 5)
cv2.imshow('CTUCCE1', erosion)

kernel = np.ones((3,3),np.uint8) 
erosion = cv2.dilate(img, kernel, iterations = 5)
cv2.imshow('CTUCCE2', erosion)

cv2.waitKey(0)
cv2.destroyAllWindows()