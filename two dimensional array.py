#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[4]:


import numpy as np


# In[ ]:


### any random value no ranging betwn 0 to 1


# In[5]:


np.random.rand(3,2)


# In[ ]:


###randn both neg and pos no (0 to 1)


# In[6]:


np.random.randn(3,2)


# In[8]:


np.random.randint(20,56,100)


# In[14]:


np.random.randint(34,100)


# In[10]:


sample_array=np.arange(30)
sample_array


# In[12]:


rand_array=np.random.randint(0,100,20)
rand_array


# In[13]:


sample_array.reshape(6,5)


# In[15]:


sample_array.reshape(4,10)


# In[16]:


rand_array.min()


# In[ ]:


###  arg means index


# In[17]:


rand_array.argmin()


# In[18]:


sample_array.dtype


# In[ ]:


### identity matrics


# In[20]:


a=np.eye(5)
a


# In[24]:


a.T


# In[22]:


a=np.random.rand(2,3)
a


# In[25]:


sample_array=np.arange(10,21)
sample_array


# In[26]:


sample_array[3]


# In[27]:


sample_array[3:7]


# In[29]:


sample_array[1:4]=100
sample_array


# In[30]:


sample_array=np.arange(10,21)
sample_array


# In[31]:


sample_array[0:7]


# In[33]:


subset_sample_array=sample_array[0:7]
subset_sample_array


# In[35]:


subset_sample_array[1:4]=1001
subset_sample_array


# In[36]:


subset_sample_array[:]=1001
subset_sample_array


# In[ ]:


### two dimensional array


# In[ ]:


import numpy as np


# In[37]:


sample_matrix=np.array(([50,20,1,23],[24,23,21,33],[56,74,24,7]))
sample_matrix


# In[38]:


sample_matrix[0][2]


# In[39]:


sample_matrix[2,:]


# In[40]:


sample_matrix[2]


# In[41]:


sample_matrix[:,(3,2)]


# In[ ]:


### selection techniques


# sample_array=np.arange(1,20)
# sample_array

# In[42]:


sample_array=np.arange(1,20)
sample_array


# In[43]:


sample_array


# In[44]:


sample_array+sample_array


# In[45]:


np.exp(sample_array)  #exponential


# In[46]:


np.sqrt(sample_array)


# In[47]:


np.log(sample_array)


# In[48]:


np.max(sample_array)


# In[49]:


np.min(sample_array)


# In[50]:


np.argmax(sample_array)


# In[51]:


np.argmin(sample_array)


# In[52]:


np.square(sample_array)


# In[53]:


np.std(sample_array)


# In[54]:


np.var(sample_array)


# In[55]:


np.mean(sample_array)


# In[56]:


array=np.random.randn(3,4)
array


# In[59]:


np.round(array,decimals=4)


# In[60]:


sports=np.array(['golf','cricket','fball','cricket','football'])
np.unique(sports)


# In[ ]:


### pandas To create data,table and manupulation


# In[62]:


import pandas as pd
import numpy as np


# In[61]:


labels=['w','x','y','z']
sample_list=[100,200,300,400]
array=np.array([1,2,3,4])
dict={'w':10,'x':20,'y':30,'z':40}


# In[63]:


pd.Series(data=sample_list)


# In[64]:


pd.Series(data=sample_list,index=labels)


# In[65]:


pd.Series(sample_list,labels)


# In[66]:


pd.Series(dict)


# In[ ]:


###pandas pandas dataframe and indexing 



# In[3]:


import pandas as pd
import numpy as np


# In[4]:


sports1=pd.Series([1,2,3,4],index=['cricket','football','basketball','golf'])
sports1


# In[5]:


sports1['cricket']


# In[6]:


sports2=pd.Series([11,2,3,4],index=['cricket','football','baseball','golf'])
sports2


# In[7]:


sports1+sports2


# In[8]:


df1=pd.DataFrame(np.random.randn(8,5),index='A B C D E F G H'.split(),columns='score1 score2 score3 score4 score5'.split())


# In[9]:


df1


# In[11]:


df1["score3"]


# In[12]:


df1[["score1","score2","score3"]]


# In[13]:


df1['score6']=df1['score1']+df1['score2']
df1


# In[9]:


import pandas as pd 
import numpy as np


# In[12]:


df={'id':['101','102','103','107','176'],'Name':['john','mercy','akash','kavin','lally'],'profit':[20,54,56,87,123]}
df=pd.DataFrame(df)
df


# In[13]:


df[["id","Name"]]


# In[16]:


df.drop("id",axis=1)


# In[17]:


df.drop(3)


# In[ ]:


###how to omprt Dataset using pandas


# In[ ]:


import numpy as np
import pandas as pd


# In[7]:


df=pd.read_excel("C:\Users\91723\OneDrive\Desktop\School Payment Worksheet.xls")


# In[ ]:


df.head(10)


# In[ ]:


df.tail()


# In[ ]:


df.sample(10)


# In[ ]:


df.shape


# In[ ]:


df.dtypes


# In[ ]:


df.info()


# In[ ]:


df.info

