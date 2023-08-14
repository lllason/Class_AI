import cv2

# Read in image
image = cv2.imread('opencv-fig-me01.jpg')

"""
    GaussianBlur 
    * Q: 為什麼要模糊?
    * A: 因為先做高斯模糊(或說經過高斯平滑)的圖片能夠去除很多圖片的噪聲(雜訊)，更容易讓我們找到更精準的輪廓。
"""
# Create ROI coordinates
## topLeft (左上)　bottomRight (右下)
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

## ===============================================================================================
## topLeft (左上)　bottomRight (右下)
topLeft = (160, 380)
bottomRight = (400, 480)
x, y = topLeft[0], topLeft[1]
w, h = bottomRight[0] - topLeft[0], bottomRight[1] - topLeft[1]

# Grab ROI with Numpy slicing and blur
ROI = image[y:y+h, x:x+w]
blur2 = cv2.GaussianBlur(ROI, (51,51), 0) 

# Insert ROI back into image
image[y:y+h, x:x+w] = blur2


cv2.imshow('CTUCCE3', blur2)
cv2.imshow('CTUCCE4', image)
cv2.waitKey()