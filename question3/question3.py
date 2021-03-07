# -*- coding:utf-8 -*-
from keras.models import Sequential
from keras.layers import Dense
import numpy as np
import pandas as pd

#load in train_data
x = pd.read_csv('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question3/train_data.txt',sep='\t')
y = pd.read_csv('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question3/train_truth.txt',sep='\t')
x = x.values
y = y.values

#the MLP Mode in question is squential with only neighbor layers connected
model = Sequential()

#add hidden layers and set activation function
model.add(Dense(4,input_dim=3,activation='sigmoid', use_bias=True))
model.add(Dense(4,input_dim=4,activation='sigmoid', use_bias=True))
model.add(Dense(1,input_dim=4,activation='sigmoid', use_bias=True))

#compile the model based on least squares as the loss function
model.compile(loss='mean_squared_error',optimizer='adam',metrics=['accuracy'])

#train the model
#divide 10000 data into 100 groups of 100 data, set 20% for validation
model.fit(x=x,y=y,epochs=100,batch_size=100,validation_split=0.2,verbose=0)

#load in test_data
x_test = pd.read_csv('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question3/test_data.txt',sep='\t')
x_test = x_test.values
output = pd.DataFrame(model.predict(x_test))
output.columns = ['y']
output.to_csv('/Users/zhangyuze/Desktop/AY20_MBDS_questions/question3/test_predicted.txt',header='y',index=0,sep='\t')
print('done')
