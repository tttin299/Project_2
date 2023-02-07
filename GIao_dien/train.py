# import the necessary packages
from sklearn.preprocessing import LabelBinarizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from keras.models import Sequential
from keras.layers.core import Dense, Dropout
from keras.layers.convolutional import Conv2D
from keras.layers.convolutional import MaxPooling2D
from keras.layers import Flatten
from keras.optimizers import SGD
import keras
from imutils import paths
import matplotlib.pyplot as plt
import numpy as np
import argparse
import random
import pickle
import cv2
import os
import time
from sklearn.preprocessing import LabelEncoder
from keras.utils import to_categorical
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_json

t0 = time.time() 
# construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-d", "--dataset", default = 'dataset_characters',
#     help="path to input dataset of images")
# ap.add_argument("-m", "--model", default = 'model',
#     help="path to output trained model")
# ap.add_argument("-l", "--labelbin", default = 'labelbin',
#     help="path to output label binarizer")
# ap.add_argument("-p", "--plot", default = 'plot',
#     help="path to output accuracy/loss plot")
# args = vars(ap.parse_args())

num_classes = 36

# initialize the data and labels
print("[INFO] loading images...")
data = []
labels = []

# grab the image paths and randomly shuffle them
imagePaths = sorted(list(paths.list_images('dataset_characters')))
random.seed(42)
random.shuffle(imagePaths)

# loop over the input images
i = 0
for imagePath in imagePaths:
    
    # print(imagePath)
    # load the image, resize the image to be 32x32 pixels (ignoring
    # aspect ratio), flatten the image into 32x32x3=3072 pixel image
    # into a list, and store the image in the data list
    image = cv2.imread(imagePath,0)
    image = cv2.resize(image, (32, 32))
    image = np.reshape(image, (32, 32, 1))
    data.append(image)

    # extract the class label from the image path and update the
    # labels list
    label = imagePath.split(os.path.sep)[-2]
    labels.append(label)
    i= i + 1
    print('img: ' + str(i))

# scale the raw pixel intensities to the range [0, 1]
data = np.array(data, dtype="float") / 255.0
labels = np.array(labels)
print("[INFO] Find {:d} images with {:d} classes".format(len(data),len(set(labels))))
# # print(labels)

lb = LabelEncoder()
lb.fit(labels)
# label = lb.transform(labels)
# y = to_categorical(labels)

# save label file so we can use in another script
np.save('license_character_classes.npy', lb.classes_)
# # perform one-hot encoding on the labels
# lb = LabelEncoder()
# lb.fit(labels)
# labels = lb.transform(labels)
# y = to_categorical(labels)

# # save label file so we can use in another script
# np.save('license_character_classes.npy', lb.classes_)


# partition the data into training and testing splits using 75% of
# the data for training and the remaining 25% for testing
(trainValX, testX, trainValY, testY) = train_test_split(data,
    labels, test_size=0.2, random_state=42)

(trainX, valX, trainY, valY) = train_test_split(trainValX,
    trainValY, test_size=0.2, random_state=42)

print(trainX.shape)    
print(testX.shape)
print(trainY.shape)
print(testY.shape)

# convert the labels from integers to vectors (for 2-class, binary
# classification you should use Keras' to_categorical function
# instead as the scikit-learn's LabelBinarizer will not return a
# vector)
lb = LabelBinarizer()
trainY = lb.fit_transform(trainY)
valY = lb.transform(valY)
testY = lb.transform(testY)


# Initialising the CNN
model = Sequential()

model.add(Conv2D(32, (3, 3), input_shape = (32,32,1), activation = 'relu'))

model.add(Conv2D(32, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation = 'relu'))
model.add(Conv2D(64, (3, 3), activation = 'relu'))
model.add(MaxPooling2D(pool_size = (2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())

model.add(Dense(units = 128, activation = 'relu'))
model.add(Dropout(0.5))
model.add(Dense(units = num_classes, activation = 'softmax'))

model.summary()
# initialize our initial learning rate and # of epochs to train for
INIT_LR = 0.0001
EPOCHS = 40

# Compiling the CNN
opt = keras.optimizers.RMSprop(lr=INIT_LR, decay=1e-6)
model.compile(optimizer = opt, loss = 'categorical_crossentropy', metrics = ['accuracy'])

t1 = time.time()
# Part 2 - Fitting the CNN to the images
H = model.fit(trainX, trainY, validation_data=(valX, valY), epochs=EPOCHS, batch_size=32)

# save the model
print("Trainning time: " + str(time.time()-t1))
print("Total time: " + str(time.time()-t0))


# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model_weight.h5")
print("Saved model to disk")



# model.save(args["model"])
# evaluate the network
print("[INFO] evaluating network...")
predictions = model.predict(testX, batch_size=32)
print(classification_report(testY.argmax(axis=1),
    predictions.argmax(axis=1), target_names=lb.classes_))

# plot the training loss and accuracy
N = np.arange(0, EPOCHS)
plt.style.use("ggplot")
plt.figure()

plt.plot(N, H.history["loss"], label="train_loss")
plt.plot(N, H.history["val_loss"], label="val_loss")
plt.plot(N, H.history["accuracy"], label="train_acc")
plt.plot(N, H.history["val_accuracy"], label="val_acc")

plt.title("Training Loss and Accuracy (Simple NN)")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend()
plt.savefig("plot")

# save label binarizer to disk
print("[INFO] serializing network and label binarizer...")

# f = open(args["labelbin"], "rb")

# f = open(args["labelbin"])
# f.write(pickle.dumps(lb))
# f.close()

plt.show()

