import cv2
import matplotlib.pyplot as plt
  
# img = cv2.imread('opencv-fig3-contour.jpg')  
img = cv2.imread('keyboard.jpg')  
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray  = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
cv2.imshow("gray",img_gray)

ret, img_binary = cv2.threshold(img_gray, 225, 255, cv2.THRESH_BINARY_INV)
plt.imshow(img_binary, cmap="gray")
plt.show() 

## findContours (找輪廍) RETR_TREE 找到內部/ EXTERNAL 只找表層
contours, hierarchy = cv2.findContours(img_binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
img_contour = cv2.drawContours(img, contours, -1, (0, 255, 0), 2) #-1 (所有都顥示) 0 1 2 

cv2.imshow("img", img_contour)  
cv2.waitKey(0)  