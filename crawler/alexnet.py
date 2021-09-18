
# -*- coding:utf-8 -*-
#
# AlexNet model
 
import tensorflow as tf
import numpy as np
 
FLAGS = tf.app.flags.FLAGS
tf.app.flags.DEFINE_integer('num_class', 10, "number of classes.")
 
#顯示網絡每一層結構的函數
def print_layer(t):
  print(t.op.name, ' ', t.get_shape().as_list())
 
def alexnet(images):
    # conv1
    with tf.name_scope('conv1') as scope:
        kernel = tf.Variable(tf.truncated_normal([11,11,3,64], stddev=0.1), name='weights')
        biases = tf.Variable(tf.constant(0.0, shape=[64], trainable=True, name='biases')
        conv_plus_b = tf.nn.bias_add(tf.nn.conv2d(images, kernel, [1,4,4,1], padding='SAME'), biases)
        conv1 = tf.nn.relu(conv_plus_b, name=scope)
        print_layer(conv1)
 
    # LRN層, pool層
    lrn1 = tf.nn.lrn(conv1, 4, bias=1.0, alpha=0.001/9, beta=0.75, name='lrn1')
    pool1 = tf.nn.max_pool(lrn1, ksize=[1,3,3,1], strides=[1,2,2,1], padding='VALID', name='pool1')
 
    # conv2
    with tf.name_scope('conv2') as scope:
        kernel = tf.Variable(tf.truncated_normal([5,5,64,192], stddev=0.1), name='weights')
        biases = tf.Variable(tf.constant(0.0, shape=[192]), trainable=True, name='biases')
        conv_plus_b = tf.nn.bias_add(tf.nn.conv2d(pool1, kernel, [1,1,1,1], padding='SAME'), biases)
        conv2 = tf.nn.relu(conv_plus_b, name=scope)
 
    # LRN層, pool層
    lrn2 = tf.nn.lrn(conv2, 4, bias=1.0, alpha=0.001/9, beta=0.75, name='lrn2')
    pool2 = tf.nn.max_pool(lrn2, ksize=[1,3,3,1], strides=[1,2,2,1], padding='VALID', name='pool2')
 
    # conv3
    with tf.name_scope('conv3') as scope:
        kernel = tf.Variable(tf.truncated_normal([3,3,192,384], stddev=0.1), name='weights')
        biases = tf.Variable(tf.constant(0.0, shape=[384]), trainable=True, name='biases')
        conv_plus_b = tf.nn.bias_add(tf.nn.conv2d(pool2, kernel, [1,1,1,1], padding='SAME'), biases)
        conv3 = tf.nn.relu(conv_plus_b, name=scope)
 
    # conv4
    with tf.name_scope('conv4') as scope:
        kernel = tf.Variable(tf.truncated_normal([3,3,384,256], stddev=0.1), name='weights')
        biases = tf.Variable(tf.constant(0.0, shape=[256]), trainable=True, name='biases')
        conv_plus_b = tf.nn.bias_add(tf.nn.conv2d(conv3, kernel, [1,1,1,1], padding='SAME'), biases)
        conv4 = tf.nn.relu(conv_plus_b, name=scope)
 
    # conv5
    with tf.name_scope('conv5') as scope:
        kernel = tf.Variable(tf.truncated_normal([3,3,256,256], stddev=0.1), name='weights')
        biases = tf.Variable(tf.constant(0.0, shape=[256]), trainable=True, name='biases')
        conv_plus_b = tf.nn.bias_add(tf.nn.conv2d(conv4, kernel, [1,1,1,1], padding='SAME'), biases)
        conv5 = tf.nn.relu(conv_plus_b, name=scope)
 
    # pool5
    pool5 = tf.nn.max_pool(conv5, ksize=[1,3,3,1], strides=[1,2,2,1], padding='VALID', name='pool5')
 
    # 卷積部分到此為止,分類問題的話還有3個全連接層: 4096,4096,num_class
    with tf.name_scope('fc1') as scope:
        input_shape = pool5.get_shape().as_list()
        input_units = np.prod(input_shape[1:])
        W_fc1 = tf.Variable(tf.truncated_normal([input_units,4096], stddev=0.1, name='weight')
        b_fc1 = tf.Variable(tf.constant(0.1, shape=[4096]), name='bias')
        fc1 = tf.nn.relu(tf.matmul(tf.reshape(pool5, [-1,input_units]), W_fc1) + b_fc1, name=scope)
        fc1_drop = tf.nn.dropout(fc1, keep_prob)
 
    with tf.name_scope('fc2') as scope:
        W_fc2 = tf.Variable(tf.truncated_normal([4096,4096], stddev=0.1, name='weight')
        b_fc2 = tf.Variable(tf.constant(0.1, shape=[4096]), name='bias')
        fc2 = tf.nn.relu(tf.matmul(fc1_drop, W_fc2) + b_fc2, name=scope)
        fc2_drop = tf.nn.dropout(fc2, keep_prob)
 
    with tf.name_scope('fc3') as scope:
        W_fc3 = tf.Variable(tf.truncated_normal([4096,FLAGS.num_class], stddev=0.1, name='weight')
        b_fc3 = tf.Variable(tf.constant(0.1, shape=[FLAGS.num_class]), name='bias')
        out = tf.nn.softmax(tf.matmul(fc2_drop, W_fc3) + b_fc3)
 
    return out