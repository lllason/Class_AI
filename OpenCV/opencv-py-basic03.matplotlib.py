import cv2
import matplotlib.pyplot as plt

img= cv2.imread('opencv-fig-sample.jpg')

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()


