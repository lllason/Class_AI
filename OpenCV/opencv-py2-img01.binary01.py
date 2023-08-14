import cv2

doge = cv2.imread('opencv-fig2-taken.jpg')

grayImage = cv2.cvtColor(doge,cv2.COLOR_BGR2GRAY)
#grayImage = cv2.resize(grayImage, (300, 300), interpolation=cv2.INTER_AREA)
cv2.imshow('GRAY',grayImage)

## Binary < 127 純黑 其他純白(注意原圖亮度區)
ret,thresh1 = cv2.threshold(grayImage,127,255,cv2.THRESH_BINARY)
cv2.imshow('BINARY(127,255)',thresh1)

# ## Binary < 127 純黑 其他純白(注意原圖亮度區)
# ret,thresh1 = cv2.threshold(grayImage,50,255,cv2.THRESH_BINARY)
# cv2.imshow('BINARY2(50,255)',thresh1)

# ## Binary < 127 純黑 其他純白(注意原圖亮度區)
# ret,thresh1 = cv2.threshold(grayImage,200,255,cv2.THRESH_BINARY)
# cv2.imshow('BINARY3(200,255)',thresh1)


## Binary_Inverted < Binary顛倒，純黑區變純白／純白變純黑
ret,thresh2 = cv2.threshold(grayImage,127,200,cv2.THRESH_BINARY_INV)
cv2.imshow('BINARY_INV',thresh2)

## TRUNCATE (上下限限制:保持一定灰階)　
ret,thresh3 = cv2.threshold(grayImage,127,255,cv2.THRESH_TRUNC)
cv2.imshow('TRUNC',thresh3)

## Binary_TOZERO (減化效果潮近式)
ret,thresh4 = cv2.threshold(grayImage,127,255,cv2.THRESH_TOZERO)
cv2.imshow('BINARY_TOZERO',thresh4)

## Binary_TOZERO_INV (減化效果潮近式反向)
ret,thresh5 = cv2.threshold(grayImage,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('BINARY_TOZERO_INV',thresh5)

while True:
    k = cv2.waitKey(10)
    
    #press esc on keyboard to exit
    if k == 27:
        break

#close all the opened windows
cv2.destroyAllWindows()