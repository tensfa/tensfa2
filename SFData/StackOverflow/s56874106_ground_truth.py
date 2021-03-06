import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
import os

mnist = input_data.read_data_sets(os.path.dirname(os.path.realpath(__file__))+"/../data/MNIST_data/", one_hot=True)

x_train, y_train = mnist.train.next_batch(55000)
x_test, y_test = mnist.test.next_batch(10000)

# Reshaping the array to 4-dims so that it can work with the Keras API
x_train = x_train.reshape(x_train.shape[0], 784)
x_test = x_test.reshape(x_test.shape[0], 784)


class NeuralNetwork:
    def add_layer(inputs, in_size, out_size, activation_function=None):
        Weights = tf.Variable(tf.random_normal([in_size, out_size]))
        biases = tf.Variable(tf.zeros([out_size]) + 0.1)
        Wx_plus_b = tf.matmul(inputs, Weights) + biases
        if activation_function is None:
            outputs = Wx_plus_b
        else:
            outputs = activation_function(Wx_plus_b)
        return outputs


xs = tf.placeholder(tf.float32, [None, 784])
ys = tf.placeholder(tf.float32, [55000, 10])

l1 = NeuralNetwork.add_layer(xs, 784, 10, activation_function=None)

prediction = NeuralNetwork.add_layer(l1, 10, 1, activation_function=None)

loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                      reduction_indices=[1]))
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

init = tf.global_variables_initializer()

sess = tf.Session()
sess.run(init)

for i in range(1):
    sess.run(train_step, feed_dict={xs:x_train, ys:y_train})
    if i % 50==0: #print loss every 50 step
        print("loss after training =",
              sess.run(loss, feed_dict={xs:x_train,ys:y_train}))