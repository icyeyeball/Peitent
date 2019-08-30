# -*- coding: utf-8 -*-
############################
# Peicheng Lu 201908230
############################
# python fuzzy.py txt
import gensim
import sys
import re

def main():
    cop = re.compile("[^\u4e00-\u9fa5^A-Z^a-z^]")
    content = sys.argv[1]
    content  = cop.sub('', content )
    word = ""
    model = gensim.models.Word2Vec.load('../word2vec_20190801.model')
    for i in range(0,len(content)):
        for j in range(0,len(content)-i):
            word = content[j:j+i+1]
            try:
                semi = model.most_similar(word)
            except KeyError:
                print ('XXXXXXXXX'+ word)
            else:
                print ('OOOOOOO'+ word)

if __name__ == "__main__":
    main()
