# enroll label -> deep_learning_model interior themes

# python image library
from PIL import Image
import os, glob, numpy as np
# divide train and test dataset
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

np.random.seed(5)
from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

# generate more images to enhance the efficiency
def generate_more_img(category_list, label_num):

    for idx, category_name in enumerate(category_list):
        img_each_dir = image_base_dir + "/" + category_name
        img_files = glob.glob(img_each_dir + "/*.jpg")

        for i, f in enumerate(img_files):
            # call dataset
            data_aug_gen = ImageDataGenerator(rescale=1./255,
                                              rotation_range=15,
                                              width_shift_range=0.1,
                                              height_shift_range=0.1,
                                              shear_range=0.5,
                                              zoom_range=[0.8, 0.2],
                                              horizontal_flip=True,
                                              vertical_flip=True,
                                              fill_mode="nearest")

            img = load_img(f)
            x = img_to_array(img)
            x = x.reshape((1,) + x.shape)

            i = 1

            # control eternal loop by break
            for batch in data_aug_gen.flow(x,
                                           batch_size=1,
                                           save_to_dir='C:/cafe-img/' + category_name,
                                           save_prefix='plus_' + str(i),
                                           save_format='jpg'):
                i += 1
                # generate 5 more images for every images
                if i > 6:
                    break

generate_more_img(category, nb_classes)
exit()

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
np.save("./dataset/deep_learning_model-img-classification-dataset.npy", (X_train, X_test, Y_train, Y_test))

print("terminate making dataset / length of train_Y -> ", len(train_Y))

# preparation for learning
config = tf.ConfigProto()
config.gpu_options.allow_growth = True
session = tf.Session(config=config)

# load saved dataset
X_train, X_test, Y_train, Y_test = np.load("./dataset/deep_learning_model-img-classification-dataset.npy")

# generalization
# astype -> convert int into float
X_train = X_train.astype(float) / 255
X_test = X_test.astype(float) / 255

with K.tf_ops.device("/device:GPU:0"):
    model = Sequential()
    # define filter, kernel size, strides, padding type, input shape, activation function

    # 1
    model.add(Conv2D(32, (3, 3), padding="same", input_shape=X_train.shape[1:], activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    # 2
    model.add(Conv2D(64, (3, 3), padding="same", activation="relu"))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Dropout(0.25))

    model.add(Flatten())
    model.add(Dense(256, activation="relu"))
    model.add(Dropout(0.25))
    model.add(Dense(nb_classes, activation="softmax"))

    # compile
    model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

    model_dir = "./model"

    # make directory if it's not exist
    if not os.path.exists(model_dir):
        os.mkdir(model_dir)

    model_path = model_dir + "/cafe-img-classification.model"
    check_point = ModelCheckpoint(filepath=model_path, monitor="val_loss", verbose=1, save_best_only=True)

    # operated when efficiency of model is not getting better results
    early_stopping = EarlyStopping(monitor="val_loss", patience=6)

    # learning process by train dataset
    history = model.fit(X_train,
                        Y_train,
                        batch_size=32,
                        epochs=50,
                        validation_data=(X_test, Y_test),
                        callbacks=[check_point, early_stopping])

    # check accuracy by test dataset
    print("accuracy : %.4f" % (model.evaluate(X_test, Y_test)[1]))

    y_vloss = history.history['val_loss']
    y_loss = history.history['loss']

    x_len = np.arange(len(y_loss))

    # check by graph
    plt.plot(x_len, y_vloss, marker='.', c='red', label='val_set_loss')
    plt.plot(x_len, y_loss, marker='.', c='blue', label='train_set_oss')
    plt.legend()
    plt.xlabel('epochs')
    plt.ylabel('loss')
    plt.grid()
    plt.show()














