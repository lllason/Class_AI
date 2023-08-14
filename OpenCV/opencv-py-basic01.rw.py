import numpy as np
import cv2


img = cv2.imread('opencv-fig-sample.jpg')

cv2.imwrite('opencv-fig-output.jpg', img)
cv2.imwrite('opencv-fig-output.png', img)
cv2.imwrite('opencv-fig-output.tiff', img)

img_gray = cv2.imread('opencv-fig-sample.jpg', cv2.IMREAD_GRAYSCALE)
img_gray = cv2.resize(img_gray, (600,400))

cv2.imwrite('opencv-fig-output.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
cv2.imwrite('opencv-fig-output.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 5])

cv2.imshow('CTUCCE', img)
cv2.imshow('CTUCCE2', img_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
