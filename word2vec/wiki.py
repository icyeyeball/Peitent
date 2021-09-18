# -*- coding: utf-8 -*-
############################
# Peicheng Lu 20190822
############################
# python wiki.py wiki_database

import logging
import sys

from gensim.corpora import WikiCorpus

def main():
    """
    if len(sys.argv) != 2:
        print("Usage: python3 " + sys.argv[0] + "wiki_data_path")
        exit()
    """
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    wiki_corpus = WikiCorpus("../large_files/zhwiki-latest-pages-articles.xml.bz2", lemmatize=False ,dictionary={})
    texts_num = 0

    with open("../large_files/wiki_texts.txt",'w',encoding='utf-8') as output:
        for text in wiki_corpus.get_texts():
            output.write(' '.join(text) + '\n')
            texts_num += 1
            if texts_num % 1000 == 0:
                logging.info("已處理 %d 篇文章" % texts_num)

if __name__ == "__main__":
    main()
