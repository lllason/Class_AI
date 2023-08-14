# Class_AI
# about AI class 

## 辨識
## OpenCV
*  Date     : 2023/08/14
*　rw       : 讀寫檔案，轉存成 jpg/png/tiff，灰階處理
*　color    : img[100,100,0] (y,x,color）　指定位置和一般不同，是 y,x color = 0,1,2(BGR index)
*  plt      : matplotlib（統計圖表）
*  camera   : 讀取鏡頭／檔案
    ** waitKey(delay) delay 調大讓等待時間足夠
*  equalizeHis : 等化(灰階等化是常用方法)
    ** equalizeHist (等化)
    ** 影像處理中常用的圖像增強技巧，
    ** 用數值方法將圖片的size變大，增加圖片對比度(CLAHE)
*  GaussianBlur : 高斯濾波(模糊)
    ** Q: 為什麼要模糊?
    ** A: 因為先做高斯模糊(或說經過高斯平滑)的圖片能夠去除很多圖片的噪聲(雜訊)，更容易讓我們找到更精準的輪廓。

## 
