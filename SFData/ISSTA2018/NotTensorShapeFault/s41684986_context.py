import tensorflow as tf
import numpy as np

x = tf.placeholder(tf.float32, [3, 4])
y = tf.placeholder(tf.int32, [4, 5])
z = tf.matmul(x, y)
init = tf.initialize_all_variables()

sess = tf.Session()
sess.run(init)
print(sess.run(z, feed_dict={x: np.random.uniform(0, 10, [3, 4]), y: np.random.randint(0, 10, [4, 5])}))