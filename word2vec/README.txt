Large files:
https://drive.google.com/drive/folders/1ELeGUV6xF75hXCDW3fLeydo5IJms4KTZ?usp=sharing


python wiki.py zhwiki-20190801-pages-articles.xml.bz2 # Parse wiki database
python s2zh.py # simplified to traditional
python segment.py # Jieba
python train.py # train word2vec model

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

---Install opencc (Failed)---
Download from google-drive peitent---
put it in Pythonxx/Lib
cmd: pip install opencc-python

