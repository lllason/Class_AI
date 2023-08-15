import cv2
from matplotlib import pyplot as plt
 
def nothing(x):
    pass

# 讀入圖
img_noblur = cv2.imread('opencv-fig3-fruit.jpg', 0)
# 模糊
img = cv2.blur(img_noblur, (7,7))
# 抓線條
canny_edge = cv2.Canny(img, 0, 0)
# 秀原圖
cv2.imshow('image', img)
# 秀輪廓圖
cv2.imshow('canny_edge', canny_edge)

# 拖拉BAR 執行nothing,不會改變任何事 
cv2.createTrackbar('min_value','canny_edge',0,500,nothing)
cv2.createTrackbar('max_value','canny_edge',0,500,nothing)

# 變動方式在迴圈內處理,在這調整 max & min 和重繪圖
while(1):
    cv2.imshow('image', img)
    cv2.imshow('canny_edge', canny_edge)
    min_value = cv2.getTrackbarPos('min_value', 'canny_edge')
    max_value = cv2.getTrackbarPos('max_value', 'canny_edge')
    canny_edge = cv2.Canny(img, min_value, max_value)
    k = cv2.waitKey(10)
    if k == 27:
        break
