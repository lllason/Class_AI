from numpy import asarray
from numpy import unique
from numpy import argmax
from tensorflow.keras.datasets.mnist import load_data
from tensorflow.keras.models import load_model

(x_train, y_train), (x_test, y_test) = load_data()

model = load_model("model.h5")
image = x_train[6]
yhat = model.predict(asarray([image]))
print(yhat)
print('Predicted: class=%d' % argmax(yhat))