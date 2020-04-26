import numpy as np
import pandas as pd
import keras
from keras.utils import np_utils

(x_Train, y_Train),(x_Test, y_Test) = keras.datasets.mnist.load_data()

x_Train4D=x_Train.reshape(x_Train.shape[0],28,28,1).astype('float32')
x_Test4D=x_Test.reshape(x_Test.shape[0],28,28,1).astype('float32')
#print(x_Train4D.shape)
x_Train4D_normalize = x_Train4D/255
x_Test4D_normalize = x_Test4D/255

y_TrainOneHot = np_utils.to_categorical(y_Train)
y_TestOneHot = np_utils.to_categorical(y_Test)
print(y_Train)