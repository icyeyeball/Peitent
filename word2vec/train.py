# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
#

import logging
from gensim.models import word2vec
import os
import tensorflow as tf
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

gpu_options = tf.GPUOptions(per_process_gpu_memory_fraction=0.9)
sess = tf.Session(config=tf.ConfigProto(gpu_options=gpu_options))

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.LineSentence("../large_files/wiki_seg.txt")
    # Set values for various parameters
num_features = 300    # Word vector dimensionality 
min_word_count = 5   # Minimum word count                        
num_workers = 4       # Number of threads to run in parallel
context = 10          # Context window size                                                                                    
downsampling = 1e-3   # Downsample setting for frequent words

model = word2vec.Word2Vec(sentences, workers=num_workers, size=num_features, min_count = min_word_count, window = context, sample = downsampling)

model.init_sims(replace=True)
    
#保存模型，供日後使用 
model.save("word2vec_20201214.model")

#模型讀取方式
# model = word2vec.Word2Vec.load("your_model_name")
