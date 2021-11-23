#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[19]:


df = "https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"


# In[20]:


data = pd.read_csv(df)


# In[21]:


data.head()


# In[22]:


print(data.duplicated().value_counts())


# In[23]:


Data = data[['continent','year','lifeExp']]


# In[26]:


print(Data)


# In[11]:


dat = pd.pivot_table(Data,index='continent',columns='year',values='lifeExp')


# In[12]:


print(dat)


# In[28]:


plt.figure(figsize=(6,6))
sns.heatmap(dat,annot=True).get_figure().savefig('HeatMap.png')  
plt.title("Year vs Age - Sex Ratio")
plt.ylabel("Age range")
plt.xlabel("Year")
plt.show()


# In[ ]:





# In[ ]:




