import cv2

img = cv2.imread('opencv-fig3-Lenna.jpg')
#cv2.imshow('Origin Img ', img)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow('img_gray', img_gray)

img_blur = cv2.GaussianBlur(img_gray, (5, 5), 0)
#cv2.imshow('img_blur', img_blur)

## Canny (灰階圖,min,max) min提升,range 變少,線條變少
## 30 , 150
img_canny = cv2.Canny(img_blur, 30, 150)
cv2.imshow('Origin 30_150', img_canny)

## max down (上限下降，合格的線變多)
img_canny = cv2.Canny(img_blur, 30, 100)
cv2.imshow('MaxDown 100_100', img_canny)

## max down (上限下降，合格的線變多)
img_canny = cv2.Canny(img_blur, 30, 200)
cv2.imshow('MaxDown 100_100', img_canny)

## min up　(下限上升，合格的線變少)
img_canny = cv2.Canny(img_blur, 100, 150)
cv2.imshow('MinUp 100_150', img_canny)

## min down　(下限上升，合格的線變少)
img_canny = cv2.Canny(img_blur, 10, 150)
cv2.imshow('MinUp 10_150', img_canny)


#cv2.imshow('Result', img_canny)
cv2.waitKey(0)