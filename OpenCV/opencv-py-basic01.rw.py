import numpy as np
import cv2


img = cv2.imread('opencv-fig-sample.jpg')

## 存入三個檔案，型態為　jpg,png,tiff
cv2.imwrite('opencv-fig-output.jpg', img)
cv2.imwrite('opencv-fig-output.png', img)
cv2.imwrite('opencv-fig-output.tiff', img)

img_gray = cv2.imread('opencv-fig-sample.jpg', cv2.IMREAD_GRAYSCALE)
img_gray = cv2.resize(img_gray, (600,400))

"""
    JPEG，其表示的是图像的质量，用0-100的整数表示，默认为95。 注意，cv2.IMWRITE_JPEG_QUALITY类型为Long，必须转换成int。
    PNG，第三个参数表示的是压缩级别。cv2.IMWRITE_PNG_COMPRESSION，从0到9,压缩级别越高，图像尺寸越小。默认级别为3。
"""
cv2.imwrite('opencv-fig-output.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 90])
cv2.imwrite('opencv-fig-output.png', img, [cv2.IMWRITE_PNG_COMPRESSION, 5])

#cv2.imshow('CTUCCE', img)
#cv2.imshow('CTUCCE2', img_gray)

## add practice
img = cv2.imread('opencv-fig-output.jpg')
cv2.imshow('CTUCCE3', img)

img = cv2.imread('opencv-fig-output.png')
cv2.imshow('CTUCCE4', img)

img = cv2.imread('opencv-fig-output.tiff')
cv2.imshow('CTUCCE5', img)

cv2.waitKey(0)
cv2.destroyAllWindows()