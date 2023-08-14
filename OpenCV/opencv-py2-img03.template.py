import cv2
import numpy as np
from matplotlib import pyplot as plt

"""
    模板匹配(match template)是一種用於尋找與模板圖像（補丁）匹配（相似）的圖像區域的技術。
    需要兩張圖片:
    原始圖片: 希望在其中找到與模板圖片匹配的位置
    模板圖片: 用來與原始圖片匹配的圖片(較小張圖片)，可以視為樣本
"""

img = cv2.imread('opencv-fig2-board.jpg',0)
img2 = img.copy()
template = cv2.imread('opencv-fig2-board3.jpg',0)
template = cv2.resize(template, (150, 150), interpolation=cv2.INTER_AREA)

w, h = template.shape[::-1]

# All the 6 methods for comparison in a list (六種演算法)
methods = ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
            'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

## 依次用各種方法找出比對圖
for meth in methods:
    img = img2.copy()
    method = eval(meth)
    print(method)
    # Apply template Matching
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

    # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(img, top_left, bottom_right, (255), 5)

    #121 ("一列二欄 1號圖")
    plt.subplot(121),plt.imshow(res, cmap = 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    #121 ("一列二欄 2號圖")
    plt.subplot(122),plt.imshow(img, cmap = 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.suptitle(meth)

    plt.show()