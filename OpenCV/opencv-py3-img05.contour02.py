import cv2
import numpy as np

img = cv2.imread("opencv-fig3-contour2.jpg")

cv2.imshow("Original", img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
## 先做高斯模糊
img_blur = cv2.GaussianBlur(img_gray, (5,5), 0)

cv2.imshow("Gaussian", img_blur)

## Canny = dilate & erode
img_canny = cv2.Canny(img_blur, 70, 150)  
#img_dilate = cv2.dilate(img_canny, None, iterations=1)
#img_erode = cv2.erode(img_dilate, None, iterations=1)

# 找輪廍
cnts, hierarchy = cv2.findContours(img_canny.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#cnts, hierarchy = cv2.findContours(img_canny.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

print("Counting {} shapes in this image". format(len(cnts)))

img_contours = img.copy()
cv2.drawContours(img_contours, cnts, -1, (0, 0, 0), 2)

# loop over the contours individually
img_centroid = img.copy()

## 找質心（多個） moments (中心點座標)
for c in cnts:
    print(cv2.contourArea(c))
    print(cv2.arcLength(c,True))

    M = cv2.moments(c)  
    cx = int(M["m10"]/M["m00"])
    cy = int(M["m01"]/M["m00"])
    cv2.circle(img_centroid, (cx, cy), 5, (0, 0, 255), -1)

img_result = np.hstack([img_contours, img_centroid])
cv2.imshow("Result", img_result)
cv2.waitKey(0)