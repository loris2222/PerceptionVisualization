import pandas as pd
import numpy as np
from PIL import Image
import os
import importdataset
from keras import applications, Input
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPool2D
from keras.layers import GlobalAveragePooling2D, AveragePooling2D, Flatten, Conv2DTranspose
from keras.models import Sequential, Model, load_model
from keras.optimizers import SGD, Adam
from tensorflow.keras.losses import MeanSquaredError, BinaryCrossentropy
from keras import metrics
from keras import losses
from keras.models import Sequential
import keras.backend as K
from PIL import Image
from PIL import ImageTk, ImageWin
import tkinter
import keras
from bpmll import bp_mll_loss
import utils
import h5py
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import cv2

physical_devices = tf.config.list_physical_devices('GPU')
tf.config.experimental.set_memory_growth(physical_devices[0], True)

basepath = os.getcwd()
decoder_path = os.path.join(basepath, "../models/decoder")
classifier_path = os.path.join(basepath, "../models/classifier")
main_dataset_path = os.path.join(basepath, "../datasets/dataset.h5")
encoder_dataset_path = os.path.join(basepath, "../datasets/dataset_encoder.h5")

decoder = keras.models.load_model(decoder_path, custom_objects={"bp_mll_loss": bp_mll_loss,
                                                            "euclidean_distance_loss": utils.euclidean_distance_loss})

classifier = keras.models.load_model(classifier_path, custom_objects={"bp_mll_loss": bp_mll_loss, "euclidean_distance_loss": utils.euclidean_distance_loss})

decoder.summary()
classifier.summary()

# Load targets (The targets for the decoder are the original inputs, X in main dataset)
hf = h5py.File(main_dataset_path, 'r')
# Y_train = hf.get('X_Train').value
Y_test = hf.get('X_Test').value

# Load inputs(The outputs of the encoder, E in encoder dataset)
hf.close()
hf = h5py.File(encoder_dataset_path, 'r')
# X_train = hf.get('E_train').value
X_test = hf.get('E_test').value
hf.close()


root = tkinter.Tk()
root.geometry('1000x1000')
canvas = tkinter.Canvas(root, width=999, height=999)
canvas.pack()

for i in range(20, 40):
    y = ((decoder.predict(X_test[i:i+1, :, :, :]))*255).squeeze().astype(np.uint8)
    x = (Y_test[i:i+1, :, :, :]*255).squeeze().astype(np.uint8)
    res = np.concatenate((x, y), axis=1)
    print("Model prediction")
    classes = classifier.predict(Y_test[i:i+1, :, :, :]).squeeze()
    print(classes)
    accepted = []
    count = 0
    for elem in importdataset.CLASS_NAMES:
        if elem == "person":  # classes[count] > 0.1:
            accepted.append((elem, classes[count]))
        count += 1
    image = Image.fromarray(res)
    image = ImageTk.PhotoImage(image)
    imagesprite = canvas.create_image(400, 400, image=image)
    root.update()
    print(accepted)
    input("Any key to continue")



































