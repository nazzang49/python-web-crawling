from tensorflow.python.client import device_lib
import tensorflow as tf

device_lib.list_local_devices()
gpus = tf.config.experimental.list_physical_devices('GPU')
print(gpus)