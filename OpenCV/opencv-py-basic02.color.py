import numpy as np
import cv2 as cv

img = cv.imread('opencv-fig-sample.jpg')

px = img[100,100]
print( px )
#[57 63 68]

blue = img[100,100,0]
print( blue )
#57

green = img[100,100,1]
print( green )
#

red = img[100,100,2]
print( red )
#

img[100,100] = [255,255,255]
print( img[100,100] )
#[255 255 255]
