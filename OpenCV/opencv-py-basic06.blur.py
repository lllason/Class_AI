import cv2

# Read in image
image = cv2.imread('opencv-fig-me01.jpg')

# Create ROI coordinates
topLeft = (60, 140)
bottomRight = (340, 250)
x, y = topLeft[0], topLeft[1]
w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]

# Grab ROI with Numpy slicing and blur
ROI = image[y:y+h, x:x+w]
blur = cv2.GaussianBlur(ROI, (51,51), 0) 

# Insert ROI back into image
image[y:y+h, x:x+w] = blur

cv2.imshow('CTUCCE1', blur)
cv2.imshow('CTUCCE2', image)
cv2.waitKey()