Large files:
https://drive.google.com/drive/folders/1ELeGUV6xF75hXCDW3fLeydo5IJms4KTZ?usp=sharing
From wiki Chinese database:
zhwiki-20190801-pages-articles.xml.bz2 --wiki.py-->wiki_tests.txt--(split -n 10 wiki_tests.txt wiki)--do.sh(s2zh.py)--cat wiki* wiki_zh.txt-->wiki_zh.txt --segment.py-->wiki_seg.txt --train.py-->word2vec_20190801(model)
===============================================
python wiki.py zhwiki-20190801-pages-articles.xml.bz2 # Parse wiki database
python s2zh.py # simplified to traditional
python segment.py # Jieba
python train.py # train word2vec model
python demo.py # demo.py must be utf-8

---In Anaconda Prompt, do:---
conda create --name tensorflow python=x.x anaconda
activate tensorflow
pip install tensorflow
python -m pip install --upgrade pip
conda update ipython
conda create --name tensorflow-gpu python=x.x anaconda
activate tensorflow-gpu
pip install tensorflow-gpu
python -m pip install --upgrade pip
conda update ipython

---(change python 3.7 to 3.6)---
/usr/local/lib/python3.7/site-packages/tensorflow/python/pywrap_tensorflow_internal.py
================================================
---Install opencc (Failed)---
Download from google-drive peitent---
put it in Pythonxx/Lib
cmd: pip install opencc-python

