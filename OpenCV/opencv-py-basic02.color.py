import numpy as np
import cv2 as cv

img = cv.imread('opencv-fig-sample.jpg')

## OpenCV color Style : (BGR) 
## [100,100,0] (y,x,color) color = 0,1,2(BGR)
px = img[100,100] 
print( px )
#[57 63 68]

blue = img[100,100,0]
print( blue )
#57

green = img[100,100,1]
print( green )
#63

red = img[100,100,2]
print( red )
#68

## 重新填色
img[110,100] = [255,255,255]
img[100,100] = [255,255,0]
img[110,90] = [0,255,255]
img[100,90] = [255,0,255]




print( img[100,100] )
#[255 255 255]

cv.imshow('CTUCCE', img)

cv.waitKey(0)
cv.destroyAllWindows()