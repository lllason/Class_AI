import cv2

img = cv2.imread('opencv-fig3-Lenna.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('img_gray', img_gray)

img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
cv2.imshow('img_blur', img_blur)

img_canny = cv2.Canny(img_blur, 30, 150)
cv2.imshow('img_canny', img_canny)

cv2.imshow('Input', img)
#cv2.imshow('Result', img_canny)
cv2.waitKey(0)