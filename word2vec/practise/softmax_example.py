# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# 
import tensorflow as tf
import math
import numpy as np



def __is_bounded(direction,range,index,tokens_leng):
    cover = range*direction
    if cover+index<0 or cover+index >= tokens_leng:
        return True
    else:
        return False

def get_context(tokens, window_size):
    context_pair = []
    for i, token in enumerate(tokens):
        for j in range(1, window_size+1):
            if not __is_bounded(1,j,i,len(tokens)):
                context_pair.append((tokens[i],tokens[i+j]))
            if not __is_bounded(-1,j,i,len(tokens)):
                context_pair.append((tokens[i],tokens[i-j]))
    return context_pair

def __get_word_set(tokens):
    word_set = set()
    for token in tokens:
        word_set.add(token)
    return word_set

def __get_word_index(word_set):
    word_index_dic = dict()
    inverse_word_dic = dict()
    for i,word in enumerate(word_set):
        word_index_dic[word] = i
        inverse_word_dic[i] = word
    return word_index_dic,inverse_word_dic

def generate_batch(context_pair,batch_size):
    batch_list =[]
    batch=[]
    for i,pair in enumerate(context_pair):

        if i %batch_size==0 and i !=0:
            batch_list.append(batch)
            batch = []

        batch.append(pair)
    return batch_list

def get_vec(word,session):
    return session.run(embeddings[word_index_dic[word]])

def __dis(vec1, vec2):
    dis = 0.0
    for i in range(0,len(vec1)):
        dis+=math.pow((vec1[i]-vec2[i]),2)
    return dis

def get_cos_similarity(vec1, vec2):
    vec1_leng=0
    for value in vec1:
        vec1_leng+=(value*value)
    vec1_leng=math.sqrt(vec1_leng)
    vec2_leng=0
    for value in vec2:
        vec2_leng+=(value*value)
    vec2_leng=math.sqrt(vec2_leng)
    product=np.dot(vec1,vec2)

    return product/(vec1_leng*vec2_leng)

def __sim(vec1, vec2):
    return (1 - math.acos(get_cos_similarity(vec1,vec2)) / math.pi)

def one_hot(data, label_size):
    vector = np.zeros((len(data),label_size),dtype='f')
    for i,single in enumerate(data):
        vector[i][single]=1.0
    return vector

def find_cloest_word(word_set,session,target_word):
    sim = 0.0
    vec1 = get_vec(target_word,session)
    result = ''
    for word in word_set:
        if word == target_word:
            continue
        vec2 = get_vec(word,session)
        tmp_sim=__sim(vec1, vec2)
        print('%s : %s : %s' %(target_word,word,tmp_sim))
        if tmp_sim>sim:
            sim = tmp_sim
            result = word
    return result

text =['he is the king','the king is royal','she is the royal queen']
window_size = 2
embedding_size = 5

if __name__ == '__main__':
    context_pair=[]
    word_set = set()

    for sentence in text:
        tokens = sentence.lower().split(' ')
        context_pair += get_context(tokens,window_size)
        tmp_word_set = __get_word_set(tokens)
        for word in tmp_word_set:
            word_set.add(word)

    word_index_dic,inverse_word_dic=__get_word_index(word_set)
    word_size = len(word_set)
    batch_size = len(context_pair)
    inputs = [word_index_dic[x[0]] for x in context_pair]
    labels = [word_index_dic[x[1]] for x in context_pair]

    train_inputs = tf.placeholder(tf.int32, shape=[batch_size])
    train_labels = tf.placeholder(tf.int32, shape=[batch_size,])

    embeddings = tf.Variable(
        tf.random_uniform([word_size, embedding_size], -1.0, 1.0))
    embed = tf.nn.embedding_lookup(embeddings, train_inputs)

    nce_weights = tf.Variable(
        tf.truncated_normal([word_size,embedding_size],
                            stddev=1.0 / math.sqrt(embedding_size)))

    nce_biases = tf.Variable(tf.zeros([word_size]))

    prediction = tf.add(tf.matmul(embed, tf.transpose(nce_weights)), nce_biases)
    train_labels_vector = tf.one_hot(train_labels,word_size)

    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction, labels=train_labels_vector))
    optimizer = tf.train.GradientDescentOptimizer(learning_rate=1.0).minimize(loss)
    session = tf.Session()
    init = tf.global_variables_initializer()
    session.run(init)
    for iteration in range(0,10000):
        total_loss = 0

        feed_dict = {train_inputs: inputs, train_labels: labels}
        _, cur_loss,pred= session.run([optimizer, loss, prediction], feed_dict=feed_dict)
        print('%s: loss: %s' %(iteration,cur_loss))
    print(find_cloest_word(word_set,session,'king'))
    print(find_cloest_word(word_set, session, 'queen'))
    print(find_cloest_word(word_set, session, 'royal'))
