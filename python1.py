import tensorflow as tf
import numpy as np

#creat data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3


###create tensorflow structure start###
Weights = tf.Variable(tf.random_uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases
loss = tf.reduce_mean(tf.square(y - y_data))
optimizer = tf.train.GradientDescentOptimizer(0.5)
train = optimizer.minimize(loss)
init = tf.global_variables_initializer()
###create tensorflow structure end###

sess = tf.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))

sess.close()

#------------------------------------------------------

maxtrix1 = tf.constant([[3, 4]])
maxtrix2 = tf.constant([[2],
                        [5]])
product = tf.matmul(maxtrix1, maxtrix2)

## method1
sess = tf.Session()
result = sess.run(product)
print(result)
sess.close()

## method2
with tf.Session() as sess:
    result2 = sess.run(product)
    print(result2)

#------------------------------------------------------

state = tf.Variable(0, name = 'counter')
#print(state.name)
one = tf.constant(1)

new_value = tf.add(state, one)
update = tf.assign(state, new_value)
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for _ in range(3):
        sess.run(update)
        print(sess.run(state))




