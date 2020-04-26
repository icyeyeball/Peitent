from keras.datasets import cifar10
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import OneHotEncoder
from sklearn.metrics import accuracy_score

(x_train, y_train), (x_test, y_test) = cifar10.load_data()

print(x_train.shape) #(50000, 32, 32, 3)

## Normalize Data
def normalize(X_train,X_test):
        mean = np.mean(X_train,axis=(0,1,2,3))
        std = np.std(X_train, axis=(0, 1, 2, 3))
        X_train = (X_train-mean)/(std+1e-7)
        X_test = (X_test-mean)/(std+1e-7)
        return X_train, X_test
    
#隨機重洗training_data，每個epoch前用
def Shuffle_data(x_train, y_train):
    shuffle= list(zip(x_train, y_train))

    np.random.shuffle(shuffle)

    x_train, y_train= zip(*shuffle)
    x_train=np.array(x_train)
    y_train=np.array(y_train)
    return (x_train,y_train)

#建立Batch_data
def Train_in_Batch(x_train, y_train,batch_size):
    assert len(x_train)/batch_size==int(len(x_train)/batch_size)
    Batch_X=np.split(x_train, len(x_train)/batch_size)
    Batch_y=np.split(y_train, len(y_train)/batch_size)
    for x,y in zip(Batch_X,Batch_y):
        yield (x,y)
    
## Normalize Training and Testset    
x_train, x_test = normalize(x_train, x_test) 

## OneHot Label 由(None, 1)-(None, 10)
one_hot=OneHotEncoder()
y_train=one_hot.fit_transform(y_train).toarray()
y_test=one_hot.transform(y_test).toarray()


tf.reset_default_graph() 


def Convolution_Block(input_,filters=16,strides=(1,1),kernel_size=(3,3),padding='same'):
    #convolution層
    X=tf.layers.conv2d(inputs=input_,filters=filters,kernel_size=kernel_size,strides=strides,padding=padding)
    #Activation function
    X=tf.nn.leaky_relu(X) 
    #Batch_Normalization
    output=tf.layers.batch_normalization(X)
    return output
    

##設定Input與Label
with tf.name_scope('input'):
    inputs = tf.placeholder(tf.float32, [None, 32, 32, 3]) ##輸入為四維[Batch_size,height,width,channels] 
    y_true = tf.placeholder(tf.float32, [None, 10]) ## Onehot Label

with tf.name_scope('stem'):
    #第一層卷積組合
    X=Convolution_Block(inputs,filters=16,strides=(1,1),kernel_size=(3,3),padding='same')
    #Strides在長寬都是1，padding是same所以尺寸不變
    print(X.shape)#(?, 32, 32, 16)
    #第一層最大池化
    X=tf.nn.max_pool(X,[1,2,2,1],[1,2,2,1],padding='SAME')
    #Strides在長寬都是2，kernel_size也是2*2，padding是same所以尺寸變為1/2
    print(X.shape)
    
    #第二層卷積組合
    X=Convolution_Block(X,filters=16,strides=(1,1),kernel_size=(3,3),padding='valid')
    #Strides在長寬都是1，padding是valid所以尺寸縮小
    print(X.shape)#((?, 14, 14, 16)
    #第二層最大池化
    X=tf.nn.max_pool(X,[1,2,2,1],[1,2,2,1],padding='VALID')
    #Strides在長寬都是2，kernel_size也是2*2，padding是Valid，由於可以完整走完，所以尺寸仍變為1/2
    print(X.shape) #(?, 7, 7, 16)
    
    #第三層卷積組合
    X=Convolution_Block(X,filters=8,strides=(1,1),kernel_size=(3,3),padding='same')
    print(X.shape)#((?, 7, 7, 8)
    
    #卷積後不一定要接Maxpooling

with tf.name_scope('Flatten'):
    X =tf.layers.Flatten()(X)
    print(X.shape)#(?, 392)) 392=7*7*8
    
with tf.name_scope('FCL'):
    X=tf.layers.dense(X,100,name='dense_1')
    X=tf.nn.leaky_relu(X) 
    X=tf.layers.dropout(X,rate=0.3)
    out_put_final=tf.layers.dense(X,10,name='out_put',)
    print(out_put_final.shape)
    
with tf.name_scope('Predict'):
    # output經過softmax
    prediction=tf.nn.softmax(out_put_final)
    
with tf.name_scope('loss'):
    # tf.nn.softmax_cross_entropy_with_logits_v2-裡面概念是先做output做softmax，再與Label做cross entropy的計算
    # tf.reduce_mean平均batch的loss
    loss=tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=y_true,logits=out_put_final,name='loss_'))
    #目標就是要縮小loss，優化器使用Adam
    optim=tf.train.AdamOptimizer().minimize(loss)
    
    
#基本設定
from tqdm import tqdm_notebook #用來顯示進度條的套件，可用pip安裝
from sklearn.metrics import accuracy_score
import time
epochs = 50 #要跑多少epoch
batch_size = 100 #設定看過幾筆資料走一次更新(batch size)
iteration = int(len(x_train)/batch_size) #一個epoch要跑幾個batch

with tf.Session() as sess:
    
    sess.run(tf.global_variables_initializer())
    
    print('x_test的size: ',x_test.nbytes/1024/1024, 'Mb')

    for epoch in range(epochs):
        
        x_train,y_train=Shuffle_data(x_train, y_train)
        Batch_data=Train_in_Batch(x_train, y_train,batch_size=batch_size)

  
        training_loss = 0 
        training_acc = 0
        bar = tqdm_notebook(range(iteration)) #外面的tqdm是進度條的function
        which_pic=0
        for iter_ in bar:
            train_batch_x,train_batch_y=next(Batch_data)
            ##更新weights，以及得到prediction
            tr_pred, training_loss_batch, _ = sess.run([prediction, loss, optim], feed_dict={inputs:train_batch_x,y_true:train_batch_y,})
            training_loss += training_loss_batch

            training_acc_batch = accuracy_score(np.argmax(train_batch_y, axis=1), np.argmax(tr_pred, axis=1))
            training_acc += training_acc_batch
            if iter_ % 5 == 0:
                bar.set_description('loss: %.4g' % training_loss_batch) 
                #每5次batch更新顯示的batch loss(進度條前面)'''

        training_loss /= iteration
        training_acc /= iteration

        te_pred,testing_loss = sess.run([prediction,loss], feed_dict={inputs:x_test,y_true:y_test})

        #### calculate testing data acc ####
        testing_acc = accuracy_score(np.argmax(y_test, axis=1), np.argmax(te_pred, axis=1))
        print('Training_set accuracy: ',training_acc)
        print('Test_set accuracy: ',testing_acc)
        