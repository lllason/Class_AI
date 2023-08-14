import cv2 as cv

def edge_demo(image):
    blurred = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(blurred, cv.COLOR_RGB2GRAY)
    edge_output = cv.Canny(gray, 50, 150)
    cv.imshow("Canny Edge", edge_output)
    dst = cv.bitwise_and(image, image, mask= edge_output)
    cv.imshow("Color Edge", dst)

img = cv.imread('opencv-fig3-girl.jpg')
cv.namedWindow('Input', cv.WINDOW_NORMAL)
cv.imshow('Input', img)
edge_demo(img)

cv.waitKey(0)
cv.destroyAllWindows()
