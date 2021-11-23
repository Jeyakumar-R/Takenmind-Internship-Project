#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Load dependencies in python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
from sklearn.datasets import load_iris


# In[4]:


#Load Iris Dataset
iris=load_iris()
for keys in iris.keys() :
    print(keys)


# In[5]:


#Define X and y from dataset and split the dataset in test and train    
X=iris.data
y=iris.target


# In[6]:


from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3)


# In[7]:


#Print test and train
print('X_train')
print(X_train)
print('X_test')
print(X_test)


# In[8]:


#Import dependencies for Classifier
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier


# In[9]:


# Display the accuracy
dtc = DecisionTreeClassifier()
dtc.fit(X_train, y_train)
dtc.score(X_test, y_test)


# In[ ]:




