# enroll label -> cafe-cnn-deep-learning interior themes

# python image library -> PIL
from PIL import Image
# numpy -> necessary to make vector dataset
import os, glob, numpy as np
# divide train and test dataset -> scikit-learn
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from keras.callbacks import EarlyStopping, ModelCheckpoint
import matplotlib.pyplot as plt
import keras.backend.tensorflow_backend as K
import tensorflow as tf

image_base_dir = "C:/cafe-img"
# 13 categories
category = ["antique",
            "casual",
            "classic",
            "country",
            "eclectic",
            "environmental",
            "ethnic",
            "european",
            "industrial",
            "minimal",
            "modern",
            "romantic",
            "wooden"]
nb_classes = len(category)

# img height, width -> 64 * 64 = 4096 points
img_h = 64
img_w = 64

# 3 -> RGB color system -> 3 color value for 1 point
pixels = img_h * img_w * 3

# enroll label to img -> one hot encoding
def makeFeatureDataset(category_list, label_num):
    X = []
    Y = []

    for idx, category_name in enumerate(category_list):
        label = [0 for i in range(label_num)]
        # one hot encoding
        label[idx] = 1

        img_each_dir = image_base_dir + "/" + category_name
        img_files = glob.glob(img_each_dir + "/*.jpg")
        print(category_name, " -> ", len(img_files))

        for i, f in enumerate(img_files):
            img = Image.open(f)
            img = img.convert("RGB")
            # 64*64 -> https://076923.github.io/posts/Python-opencv-8/
            img = img.resize((img_w, img_h))
            # asarray -> https://rfriend.tistory.com/tag/np.asarray%28%29
            data = np.asarray(img)

            # input
            X.append(data)
            # output
            Y.append(label)

            # for checking
            if i % 500 == 0:
                print(i, " / ", category_name, " -> ", f)

    return X, Y

train_X, train_Y = makeFeatureDataset(category, nb_classes)

train_X = np.array(train_X)
train_Y = np.array(train_Y)

# ndarray -> whole elements should have same types = constraint
# example -> array([0, 1, 0, 0])
print("train_X type" + type(train_X))
print("train_Y type" + type(train_Y))

# divide into train and test dataset
X_train, X_test, Y_train, Y_test = train_test_split(train_X, train_Y)
np.save("./dataset/cafe-cnn-deep-learning-img-classification-dataset.npy", (X_train, X_test, Y_train, Y_test))

print("terminate making dataset / length of train_Y -> ", len(train_Y))

# preparation for learning
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)

# load saved dataset
X_train, X_test, Y_train, Y_test = np.load("./dataset/cafe-cnn-deep-learning-img-classification-dataset.npy")

# generalization
# astype -> convert int into float
X_train = X_train.astype(float) / 255
X_test = X_test.astype(float) / 255






















