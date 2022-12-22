#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt


# In[7]:


mydata=pd.read_csv("C:\Users\91723\Downloads\CardioGoodFitness-1.csv")


# In[ ]:


### sample() random one row sample(10) random 10


# In[7]:


mydata.sample(10)


# In[8]:


mydata.shape


# In[9]:


mydata.dtypes


# In[11]:


mydata.columns


# In[12]:


mydata.info()


# In[13]:


mydata.isnull().sum()


# In[ ]:


### describe only numeric coulumns


# In[6]:


mydata.describe()


# In[7]:


mydata.describe(include="all")


# In[ ]:


### sns seaborn library


# In[11]:


sns.countplot(x="Product",data=mydata)


# In[12]:


sns.countplot(x="Gender",data=mydata)


# In[13]:


sns.countplot(x="MartialStatus",data=mydata)


# In[14]:


sns.countplot(x="Product",hue="Gender",data=mydata)


# In[16]:


mydata.hist(figsize=(10,20))


# In[17]:


sns.boxplot(x="Product",y="Age",data=mydata) ## boxplot-one should be numerical


# In[1]:


sns.crosstab(mydata['Product'],mydata['Gender'])


# In[2]:


sns.pairplot(mydata,diag_kind='kde')


# In[8]:


corr=mydata.corr()
corr


# In[10]:


sns.heatmap(corr,annot=True,cmap="Y1GnBu")


# In[ ]:




