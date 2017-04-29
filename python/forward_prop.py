import numpy as np
import tensorflow as tf

b = tf.Variable(tf.zeros((100,)))
W = tf.Variable(tf.random_uniform(
    shape=(256, 100), minval=-1, maxval=1))
x_i = np.random.random(size=(32, 256))

x = tf.placeholder(tf.float32, (None, 256))

h_i = tf.tanh(tf.matmul(x, W) + b)
sess = tf.Session()
sess.run(tf.global_variables_initializer())
sess.run(h_i, {x: x_i})
