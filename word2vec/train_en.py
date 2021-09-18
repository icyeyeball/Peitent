# -*- coding: utf-8 -*-
############################
# Peicheng Lu 201908
############################
#

import logging
from gensim.models import word2vec
import os
import tensorflow as tf
import re

os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

config = tf.ConfigProto(log_device_placement=True)
config.gpu_options.per_process_gpu_memory_fraction = 0.9 # 占用GPU90%的显存 
session = tf.Session(config=config)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.LineSentence("../large_files/wiki_en_texts.txt")
           
# Set values for various parameters
num_features = 200    # Word vector dimensionality                      
min_word_count = 20   # Minimum word count                        
num_workers = 4       # Number of threads to run in parallel
context = 10          # Context window size    
downsampling = 1e-3   # Downsample setting for frequent words

model = word2vec.Word2Vec(sentences, workers=num_workers, size=num_features, min_count = min_word_count, window = context, sample = downsampling)

model.init_sims(replace=True)
    
#保存模型，供日後使用
model.save("word2vec_en_20190801.model")

#模型讀取方式
# model = word2vec.Word2Vec.load("your_model_name")
