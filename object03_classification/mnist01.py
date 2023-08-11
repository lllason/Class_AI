# example of a cnn for image classification
from numpy import asarray
from numpy import unique
from numpy import argmax
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Conv2D #
from tensorflow.keras.layers import MaxPool2D # 由近到深
from tensorflow.keras.layers import Flatten   # 二維打平變一維   
from tensorflow.keras.layers import Dropout   # 神經元刪除一點做調整

# example of loading and plotting the mnist dataset
from matplotlib import pyplot as plt

# # load dataset 
# ## 訓練資料(trianX , trainY),測試資料(testX, testy)
# (trainX, trainy), (testX, testy) = load_data()

# # summarize loaded dataset
# print('Train: X=%s, y=%s' % (trainX.shape, trainy.shape))
# print('Test: X=%s, y=%s' % (testX.shape, testy.shape))

# # plot first few images
# for i in range(2,15):
#     # define subplot
#     plt.subplot(5, 5, i+1)
#     # plot raw pixel data
#     plt.imshow(trainX[i], cmap=plt.get_cmap('Blues'))
# # show the figure

# plt.show()


# load dataset
(x_train, y_train), (x_test, y_test) = load_data()

# reshape data to have a single channel
x_train = x_train.reshape((x_train.shape[0], x_train.shape[1], x_train.shape[2], 1))
x_test = x_test.reshape((x_test.shape[0], x_test.shape[1], x_test.shape[2], 1))

# determine the shape of the input images
in_shape = x_train.shape[1:]
# determine the number of classes
n_classes = len(unique(y_train))
print(in_shape, n_classes)

# normalize pixel values
x_train = x_train.astype('float32') / 255.0
x_test = x_test.astype('float32') / 255.0

# define model
model = Sequential()

# input 第一層 Conv2D 為16 input_shape第一層要指定
model.add(Conv2D(16, (3,3), activation='relu', kernel_initializer='he_uniform', input_shape=in_shape))
model.add(MaxPool2D((2, 2)))

## 就上一層再拉一層,Conv2D 改為8
model.add(Conv2D(8, (3,3), activation='relu', kernel_initializer='he_uniform'))
model.add(MaxPool2D((2, 2)))

model.add(Flatten())
model.add(Dense(30, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(30, activation='relu', kernel_initializer='he_uniform'))
model.add(Dense(30, activation='relu', kernel_initializer='he_uniform'))

model.add(Dropout(0.2))
model.add(Dense(n_classes, activation='softmax'))

# define loss and optimizer
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# fit the model 
## (batch_size:一次抓幾張,太大記憶體會爆,太小效果不好)
history = model.fit(x_train, y_train, epochs=50, batch_size=200, verbose=1)
model.save(model.h5)

# evaluate the model
loss, acc = model.evaluate(x_test, y_test, verbose=1)
print('Accuracy: %.3f' % acc)

# make a prediction
##　argmax() 查陣列中max值
image = x_train[2]
yhat = model.predict(asarray([image]))
print(yhat)
print('Predicted: class=%d' % argmax(yhat))



plt.title("Learning Curves")
plt.xlabel('Epoch')
plt.ylabel('Loss and Accuracy')
plt.plot(history.history['loss'],label=' train loss')
plt.plot(history.history['accuracy'],label=' train accuracy')
plt.legend()
plt.show()