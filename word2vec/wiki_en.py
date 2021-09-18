# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# python wiki.py wiki_database

import logging
import sys
import warnings
warnings.filterwarnings(action='ignore', category=UserWarning, module='gensim')
import gensim
from gensim.corpora import WikiCorpus


def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    wiki_corpus = WikiCorpus("../large_files/enwiki-20190820-pages-articles-multistream.xml.bz2", lemmatize=False ,dictionary={})
    texts_num = 0

    with open("../large_files/wiki_en_texts.txt",'w',encoding='utf-8') as output:
        for text in wiki_corpus.get_texts():
            output.write(' '.join(text) + '\n')
            texts_num += 1
            if texts_num % 10000 == 0:
                logging.info("已處理 %d 篇文章" % texts_num)

if __name__ == "__main__":
    main()