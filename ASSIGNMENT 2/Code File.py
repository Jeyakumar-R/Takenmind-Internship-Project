#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from pandas import DataFrame


# In[3]:


excel = pd.ExcelFile('C:\\Users\\JEYA KUMAR R\\Downloads\\Input File.xlsx')


# In[5]:


#read excel file
df = pd.read_excel(excel,'Sheet1')
#convert excel to csv
df.to_csv('csv1.csv',sep=',')
csv = pd.read_csv('csv1.csv')


# In[6]:


#read excel file
df1 = pd.read_excel(excel,'Sheet2')
#convert excel to csv
df1.to_csv('csv2.csv',sep=',')
csv1 = pd.read_csv('csv2.csv')


# In[7]:


#read excel file
df2 = pd.read_excel(excel,'Sheet3')
#convert excel to csv
df2.to_csv('csv3.csv',sep=',')
csv2 = pd.read_csv('csv3.csv')


# In[8]:


#read excel file
df3 = pd.read_excel(excel,'Sheet4')
#convert excel to csv
df3.to_csv('csv4.csv',sep=',')
csv3 = pd.read_csv('csv4.csv')


# In[9]:


#read excel file
df4 = pd.read_excel(excel,'Sheet5')
#convert excel to csv
df4.to_csv('csv5.csv',sep=',')
csv4 = pd.read_csv('csv5.csv')


# In[10]:


#read excel file
df5 = pd.read_excel(excel,'Sheet6')
#convert excel to csv
df5.to_csv('csv6.csv',sep=',')
csv5 = pd.read_csv('csv6.csv')


# In[11]:


#read excel file
df6 = pd.read_excel(excel,'Sheet7')
#convert excel to csv
df6.to_csv('csv7.csv',sep=',')
csv6 = pd.read_csv('csv7.csv')


# In[13]:


#read excel file
df7 = pd.read_excel(excel,'Sheet8')
#convert excel to csv
df7.to_csv('csv8.csv',sep=',')
csv7 = pd.read_csv('csv8.csv')


# In[14]:


#read excel file
df8 = pd.read_excel(excel,'Sheet9')
#convert excel to csv
df8.to_csv('csv9.csv',sep=',')
csv8 = pd.read_csv('csv9.csv')


# In[15]:


#read excel file
df9 = pd.read_excel(excel,'Sheet10')
#convert excel to csv
df9.to_csv('csv10.csv',sep=',')
csv9 = pd.read_csv('csv10.csv')


# In[16]:


print(csv1)


# In[ ]:




