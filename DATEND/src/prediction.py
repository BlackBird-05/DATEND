from keras.models import load_model
import numpy as np
import keras
from keras.preprocessing import image
from keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
import cv2
import matplotlib.pyplot as plt

model = load_model('first.h5')

test_image = cv2.imread('dataset/single_prediction/eight.jpg')
test_image = cv2.resize(test_image, (28, 28))

grey_img = cv2.cvtColor(test_image, cv2.COLOR_BGR2GRAY)
reshaped = grey_img.reshape((1, 28, 28, 1))
array = np.array(grey_img)
plt.subplot(1, 1, 1)
plt.imshow(array, cmap=plt.get_cmap('gray'))
plt.show()
datagen = ImageDataGenerator(rescale = 1./255)
generated = datagen.flow(reshaped, batch_size=1)
result = model.predict(generated)
label = np.argmax(result, axis=1)


print(result)
print(label)

