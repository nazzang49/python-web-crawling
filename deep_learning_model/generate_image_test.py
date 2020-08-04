# image generating test

import glob
from keras_preprocessing.image import ImageDataGenerator, load_img, img_to_array
import os

# 3052
print(len(os.walk("C:/cafe-img-backup/environmental").__next__()[2]))
exit()

img_each_dir = "C:/cafe-img-backup/environmental"
img_files = glob.glob(img_each_dir + "/*.jpg")

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

for i, f in enumerate(img_files):

    img = load_img(f)
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)

    n = 1
    img_file_name = f.split("\\")[1].split(".")[0]
    # control eternal loop by break
    for batch in data_aug_gen.flow(x,
                                   batch_size=1,
                                   save_to_dir='C:/cafe-img-backup/environmental',
                                   save_prefix=img_file_name,
                                   save_format='jpg'):
        n += 1
        # generate 5 more images for every images
        if n > 5:
            break