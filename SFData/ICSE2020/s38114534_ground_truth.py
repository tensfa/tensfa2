import tensorflow as tf
import numpy as np

g = tf.Graph()
with g.as_default():
    # data shape is "[batch, in_height, in_width, in_channels]",
    x = tf.Variable(np.array([0.0, 0.0, 0.0, 0.0, 1.0]).reshape(1,1,-1,1), name="x")
    # filter shape is "[filter_height, filter_width, in_channels, out_channels]"
    phi = tf.Variable(np.array([0.0, 0.5, 1.0]).reshape(1,-1,1,1), name="phi")
    conv = tf.nn.conv2d(
        x,
        phi,
        strides=[1, 1, 1, 1],
        padding="SAME",
        name="conv")